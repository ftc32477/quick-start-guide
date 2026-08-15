#!/usr/bin/env python3
"""
FTC 32477 Origin 快速入门指南 — PDF 导出工具

基于 Chrome DevTools Protocol (CDP) 将 dist/ 中的 HTML 页面渲染为 PDF：
- 封面（队徽、队名、更新日期）
- 页眉（"FTC 32477 Origin 快速入门指南" + 当前章回）
- 页脚（居中"第X页，共X页"）
- 封底（居中队徽 + 右下角更新日期）
- 全部内容随语言自动本地化

用法:
    python3 build_pdf.py            # 导出所有语言的单页 PDF + 合并 PDF
    python3 build_pdf.py --lang en-us  # 仅导出指定语言（zh-hans / zh-hant / en-us / fr）
    python3 build_pdf.py --page member  # 仅导出指定页面（仅单页，不含封面封底）
    python3 build_pdf.py --rebuild  # 先执行 build.py 再导出

输出:
    dist/pdf/FTC-Team-32477-Origin-Quick-Start-Guide-{RELEASE_TAG}-{lang}.pdf  — 完整指南 PDF（封面 + 正文 + 封底），
        dist/pdf/ 不入库（.gitignore），仅供本地自查纠错；正式发布版上传为 GitHub Release 资产，
        线上主页的下载按钮指向 Release 资产链接

说明:
    - 单页 PDF（dist/pdf/{lang}/{page}.pdf，含页眉页脚）仅通过 --page 参数
      生成，用于内容调试；完整导出（不带 --page）在合并成功后会自动删除
      单页 PDF 目录，dist/pdf/ 下只保留四语言合并版指南。

依赖:
    - Google Chrome / Edge（无头模式 + 远程调试端口）
    - websocket-client（CDP 通信）: pip3 install websocket-client
    - pypdf（PDF 合并）: pip3 install pypdf
"""

import os
import sys
import time
import json
import base64
import socket
import shutil
import tempfile
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_DIR = os.path.join(BASE_DIR, "dist")
PDF_DIR = os.path.join(DIST_DIR, "pdf")
IMAGES_DIR = os.path.join(BASE_DIR, "images")

sys.path.insert(0, BASE_DIR)
import build as build_mod  # noqa: E402  复用 LANGUAGES / PAGE_KEYS / render_homepage

PAGE_KEYS = build_mod.PAGE_KEYS
LANGUAGES = list(build_mod.LANGUAGES.keys())

CHROME_CANDIDATES = [
    "/Applications/Google Chrome Dev.app/Contents/MacOS/Google Chrome Dev",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge Dev.app/Contents/MacOS/Microsoft Edge Dev",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
]

FONT_FAMILY = "-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Microsoft YaHei', 'Noto Sans SC', sans-serif"

# 封面/封底的本地化文案
PDF_TEXTS = {
    "zh-hans": {
        "badge": "TEAM 32477 ORIGIN",
        "title": "FIRST\u00ae Tech Challenge",
        "name": "32477 Origin \u5feb\u901f\u5165\u95e8\u6307\u5357",
        "name2": "Quick Start Guide",
        "school": "\u5317\u4eac\u5341\u4e00\u5b9e\u9a8c\u4e2d\u5b66",
        "date": "2026\u5e748\u6708\u7b2c1\u7248",
        "lang": "\u7b80\u4f53\u4e2d\u6587\u7248",
    },
    "zh-hant": {
        "name": "32477 Origin \u5feb\u901f\u5165\u95e8\u6307\u5357",
        "school": "\u5317\u4eac\u5341\u4e00\u5be6\u9a57\u4e2d\u5b78",
        "date": "2026\u5e748\u6708\u7b2c1\u7248",
        "lang": "\u7e41\u9ad4\u4e2d\u6587\u7248",
    },
    "en-us": {
        "name": "32477 Origin Quick Start Guide",
        "name2": "\u5feb\u901f\u5165\u95e8\u6307\u5357",
        "school": "Beijing National Day Experimental School",
        "date": "August 2026 \u00b7 1st Edition",
        "lang": "English (US) Edition",
    },
    "fr": {
        "name": "32477 Origin Guide de d\u00e9marrage rapide",
        "name2": "\u5feb\u901f\u5165\u95e8\u6307\u5357",
        "school": "Beijing National Day Experimental School",
        "date": "Ao\u00fbt 2026 \u00b7 1re \u00e9dition",
        "lang": "\u00c9dition fran\u00e7aise",
    },
}

# 目录标题本地化
TOC_TITLES = {
    "zh-hans": "\u76ee\u5f55",
    "zh-hant": "\u76ee\u9304",
    "en-us": "Table of Contents",
    "fr": "Table des mati\u00e8res",
}

# 页脚文案（reportlab 盖印，x=当前页 y=总页数）与字体（内置 CID 字体）
FOOTER_TEXTS = {
    "zh-hans": "\u7b2c {x} \u9875\uff0c\u5171 {y} \u9875",
    "zh-hant": "\u7b2c {x} \u9801\uff0c\u5171 {y} \u9801",
    "en-us": "Page {x} of {y}",
    "fr": "Page {x} sur {y}",
}
FOOTER_FONTS = {
    "zh-hans": "STSong-Light",
    "zh-hant": "MSung-Light",
    "en-us": "Helvetica",
    "fr": "Helvetica",
}

# 纸张与页边距：A4（210×297mm），上下 2.54cm，左右 3.18cm
PAPER_W_IN = 8.27   # 210mm
PAPER_H_IN = 11.69  # 297mm
MARGIN_TOP = 1.0       # 2.54cm
MARGIN_BOTTOM = 1.0    # 2.54cm
MARGIN_LEFT = 1.25     # 3.18cm
MARGIN_RIGHT = 1.25    # 3.18cm


def find_chrome():
    for path in CHROME_CANDIDATES:
        if os.path.exists(path):
            return path
    return None


def free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


# ============================================================
#  封面 / 封底 HTML（随语言本地化）
# ============================================================

def render_cover(lang_key):
    t = dict(PDF_TEXTS["zh-hans"])
    t.update(PDF_TEXTS[lang_key])
    logo_path = "file://" + os.path.join(IMAGES_DIR, "basic", "team_logo.png")
    return f"""<!DOCTYPE html>
<html lang="{lang_key}">
<head>
<meta charset="UTF-8">
<style>
@page {{ size: A4; margin: 0; }}
html,body{{margin:0;padding:0}}
.cover{{
  width:100%;height:100vh;overflow:hidden;
  background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  color:#fff;font-family:{FONT_FAMILY};position:relative;text-align:center
}}
/* 内容整体：放大并上移至黄金分割点（中心位于 38.2vh） */
.cover .inner{{
  position:relative;display:flex;flex-direction:column;align-items:center;
  transform:translateY(-11.8vh)
}}
.cover .glow{{
  position:absolute;width:420px;height:420px;border-radius:50%;
  background:#d32f2f;opacity:.14;top:-160px;right:-160px
}}
.cover img.logo{{
  width:150px;height:150px;border-radius:32px;margin-bottom:36px;
  box-shadow:0 8px 32px rgba(0,0,0,.4);position:relative
}}
.cover .badge{{
  background:#d32f2f;padding:6px 22px;border-radius:22px;
  font-size:13px;font-weight:600;letter-spacing:3px;margin-bottom:28px;position:relative
}}
.cover h1{{font-size:42px;margin:0 0 18px;font-weight:700;position:relative}}
.cover .name{{font-size:24px;font-weight:600;position:relative}}
.cover .name2{{font-size:17px;opacity:.75;margin-top:16px;position:relative}}
.cover .school{{font-size:16px;opacity:.7;margin-top:48px;position:relative}}
.cover .date{{
  position:absolute;bottom:56px;left:0;right:0;
  font-size:16px;opacity:.8;letter-spacing:2px
}}
</style>
</head>
<body>
<div class="cover">
  <div class="glow"></div>
  <div class="inner">
    <img class="logo" src="{logo_path}">
    <div class="badge">{t["badge"]}</div>
    <h1>{t["title"]}</h1>
    <div class="name">{t["name"]}</div>
    <div class="name2">{t["name2"]}</div>
    <div class="school">{t["school"]}</div>
  </div>
  <div class="date">{t["lang"]} \u00b7 {t["date"]}</div>
</div>
</body>
</html>"""


def render_back(lang_key):
    t = dict(PDF_TEXTS["zh-hans"])
    t.update(PDF_TEXTS[lang_key])
    logo_path = "file://" + os.path.join(IMAGES_DIR, "basic", "team_logo.png")
    return f"""<!DOCTYPE html>
<html lang="{lang_key}">
<head>
<meta charset="UTF-8">
<style>
@page {{ size: A4; margin: 0; }}
html,body{{margin:0;padding:0}}
/* 封底与封面镜像对称：渐变方向翻转、光斑位置镜像 */
.back{{
  width:100%;height:100vh;overflow:hidden;
  background:linear-gradient(45deg,#1a1a2e 0%,#16213e 100%);
  display:flex;align-items:center;justify-content:center;
  font-family:{FONT_FAMILY};position:relative
}}
.back .glow{{
  position:absolute;width:420px;height:420px;border-radius:50%;
  background:#d32f2f;opacity:.14;top:-160px;left:-160px
}}
.back img.logo{{
  width:61.8vw;height:61.8vw;border-radius:21.3%;opacity:.94;
  box-shadow:0 8px 32px rgba(0,0,0,.4)
}}
.back .date{{
  position:absolute;bottom:48px;right:56px;font-size:15px;color:#c9c9d4;letter-spacing:2px
}}
</style>
</head>
<body>
<div class="back">
  <div class="glow"></div>
  <img class="logo" src="{logo_path}">
  <div class="date">{t["lang"]} \u00b7 {t["date"]}</div>
</div>
</body>
</html>"""


# 版权页（封二）与资源更新页（封三）文案
IMPRINT_TEXTS = {
    "zh-hans": {
        "title_label": "\u4e66\u540d",
        "fields": [
            ("\u7248\u672c\u53f7", "{tag}"),
            ("\u7248\u6b21", "{edition}"),
            ("\u53d1\u5e03\u65e5\u671f", "{date}"),
            ("\u8bed\u8a00\u7248\u672c", "{lang_edition}"),
            ("\u4e3b\u7f16", "\u4ed8\u4fee\u9f50"),
            ("\u7f16\u59d4", "\u675c\u661f\u6d32\u3001\u8c22\u91d1\u707f \u7b49"),
            ("\u51fa\u54c1", "FTC 32477 Origin \u00b7 \u5317\u4eac\u5341\u4e00\u5b9e\u9a8c\u4e2d\u5b66"),
            ("\u5730\u5740", "\u5317\u4eac\u5e02\u6d77\u6dc0\u533a\u592a\u5e73\u8def8\u53f7 \u00b7 \u90ae\u653f\u7f16\u7801 100039"),
        ],
    },
    "zh-hant": {
        "title_label": "\u66f8\u540d",
        "fields": [
            ("\u7248\u672c\u865f", "{tag}"),
            ("\u7248\u6b21", "{edition}"),
            ("\u767c\u5e03\u65e5\u671f", "{date}"),
            ("\u8a9e\u8a00\u7248\u672c", "{lang_edition}"),
            ("\u4e3b\u7de8", "\u4ed8\u4fee\u9f4a"),
            ("\u7de8\u59d4", "\u675c\u661f\u6d32\u3001\u8b1d\u91d1\u71e6 \u7b49"),
            ("\u51fa\u54c1", "FTC 32477 Origin \u00b7 \u5317\u4eac\u5341\u4e00\u5be6\u9a57\u4e2d\u5b78"),
            ("\u5730\u5740", "\u5317\u4eac\u5e02\u6d77\u6dc0\u5340\u592a\u5e73\u8def8\u865f \u00b7 \u90f5\u901e\u5340\u865f 100039"),
        ],
    },
    "en-us": {
        "title_label": "Title",
        "fields": [
            ("Version", "{tag}"),
            ("Edition", "{edition}"),
            ("Release Date", "{date}"),
            ("Language Edition", "{lang_edition}"),
            ("Chief Editor", "Fu Xiuqi"),
            ("Editorial Board", "Du Xingzhou, Xie Jincan, et al."),
            ("Produced by", "FTC 32477 Origin \u00b7 Beijing National Day Experimental School"),
            ("Address", "No. 8 Taiping Road, Haidian District, Beijing 100039, China"),
        ],
    },
    "fr": {
        "title_label": "Titre",
        "fields": [
            ("Version", "{tag}"),
            ("\u00c9dition", "{edition}"),
            ("Date de publication", "{date}"),
            ("\u00c9dition linguistique", "{lang_edition}"),
            ("R\u00e9dacteur en chef", "Fu Xiuqi"),
            ("Comit\u00e9 de r\u00e9daction", "Du Xingzhou, Xie Jincan, et al."),
            ("Produit par", "FTC 32477 Origin \u00b7 Beijing National Day Experimental School"),
            ("Adresse", "N\u00b0 8 Taiping Road, district de Haidian, P\u00e9kin 100039, Chine"),
        ],
    },
}

RESOURCE_TEXTS = {
    "zh-hans": {
        "heading": "\u8d44\u6e90\u4e0e\u66f4\u65b0",
        "intro": "\u672c\u6307\u5357\u6301\u7eed\u4fee\u8ba2\uff0c\u53ef\u901a\u8fc7\u4ee5\u4e0b\u6e20\u9053\u83b7\u53d6\u6700\u65b0\u5185\u5bb9\uff1a",
        "items": [
            ("\u5728\u7ebf\u7248\u672c", "https://ftc32477.github.io/docs/"),
            ("\u5386\u53f2\u7248\u672c", "https://ftc32477.github.io/docs/{lang}/versions.html"),
            ("\u5f00\u6e90\u4ed3\u5e93", "https://github.com/ftc32477/quick-start-guide"),
            ("\u610f\u89c1\u53cd\u9988", "https://github.com/ftc32477/quick-start-guide/issues"),
        ],
    },
    "zh-hant": {
        "heading": "\u8cc7\u6e90\u8207\u66f4\u65b0",
        "intro": "\u672c\u6307\u5357\u6301\u7e8c\u4fee\u8a02\uff0c\u53ef\u900f\u904e\u4ee5\u4e0b\u7ba1\u9053\u53d6\u5f97\u6700\u65b0\u5167\u5bb9\uff1a",
        "items": [
            ("\u7dda\u4e0a\u7248\u672c", "https://ftc32477.github.io/docs/"),
            ("\u6b77\u53f2\u7248\u672c", "https://ftc32477.github.io/docs/{lang}/versions.html"),
            ("\u958b\u6e90\u5009\u5eab", "https://github.com/ftc32477/quick-start-guide"),
            ("\u610f\u898b\u53cd\u994b", "https://github.com/ftc32477/quick-start-guide/issues"),
        ],
    },
    "en-us": {
        "heading": "Resources & Updates",
        "intro": "This guide is revised continuously. Get the latest content through the following channels:",
        "items": [
            ("Online edition", "https://ftc32477.github.io/docs/"),
            ("Version history", "https://ftc32477.github.io/docs/{lang}/versions.html"),
            ("Open-source repository", "https://github.com/ftc32477/quick-start-guide"),
            ("Feedback", "https://github.com/ftc32477/quick-start-guide/issues"),
        ],
    },
    "fr": {
        "heading": "Ressources & Mises \u00e0 jour",
        "intro": "Ce guide est r\u00e9vis\u00e9 en continu. Obtenez les derniers contenus par les canaux suivants :",
        "items": [
            ("\u00c9dition en ligne", "https://ftc32477.github.io/docs/"),
            ("Historique des versions", "https://ftc32477.github.io/docs/{lang}/versions.html"),
            ("D\u00e9p\u00f4t open source", "https://github.com/ftc32477/quick-start-guide"),
            ("Retours", "https://github.com/ftc32477/quick-start-guide/issues"),
        ],
    },
}


def render_imprint(lang_key):
    """版权页（封二）：完整书名 / 版本号 / 版次 / 发布日期 / 编者 / 出品 / 法律声明，内容置于页面下部。"""
    t = dict(IMPRINT_TEXTS["zh-hans"])
    t.update(IMPRINT_TEXTS[lang_key])
    released = [v for v in build_mod.VERSIONS if v.get("status") != "preview"]
    latest = released[0] if released else {}
    edition = (latest.get("name", {}).get(lang_key)
               or latest.get("name", {}).get("zh-hans", ""))
    release_date = build_mod.format_release_date(lang_key, latest.get("date", ""))
    lang_edition = PDF_TEXTS[lang_key].get("lang", PDF_TEXTS["zh-hans"]["lang"])
    legal = build_mod.LANG_HOME_TEXTS[lang_key]["legal"]
    p = dict(PDF_TEXTS["zh-hans"])
    p.update(PDF_TEXTS[lang_key])
    full_title = f'{p["title"]} {p["name"]}'

    rows = (
        f'<tr><td class="k">{t["title_label"]}</td><td>{full_title}</td></tr>'
        + "".join(
            f'<tr><td class="k">{k}</td><td>{v.format(tag=latest.get("tag", ""), edition=edition, date=release_date, lang_edition=lang_edition)}</td></tr>'
            for k, v in t["fields"]
        )
    )
    return f"""<!DOCTYPE html>
<html lang="{lang_key}">
<head>
<meta charset="UTF-8">
<style>
@page {{ size: A4; margin: 0; }}
html,body{{margin:0;padding:0}}
.wrap{{
  width:100vw;height:100vh;box-sizing:border-box;padding:0.7in 0.75in;
  font-family:{FONT_FAMILY};color:#2c2c2c;
  display:flex;flex-direction:column;justify-content:flex-end
}}
table{{width:100%;border-collapse:collapse;font-size:12.5px}}
td{{padding:9px 0;vertical-align:top;border-bottom:1px solid #eee;line-height:1.7}}
td.k{{width:110px;color:#666}}
.legal{{margin-top:36px;font-size:10px;color:#9a9a9a;line-height:1.7}}
a{{overflow-wrap:anywhere;color:#2c2c2c;text-decoration:none}}
</style>
</head>
<body>
<div class="wrap">
  <table>
{rows}
  </table>
  <p class="legal">{legal}</p>
</div>
</body>
</html>"""


def render_resources(lang_key):
    """资源与更新页（封三）：获取渠道链接。"""
    t = dict(RESOURCE_TEXTS["zh-hans"])
    t.update(RESOURCE_TEXTS[lang_key])
    items = "".join(
        f'<tr><td class="k">{k}</td><td><a href="{v.format(lang=lang_key)}">{v.format(lang=lang_key)}</a></td></tr>'
        for k, v in t["items"]
    )
    return f"""<!DOCTYPE html>
<html lang="{lang_key}">
<head>
<meta charset="UTF-8">
<style>
html,body{{margin:0;padding:0}}
.wrap{{font-family:{FONT_FAMILY};color:#2c2c2c;width:100%}}
h1{{font-size:20px;color:#1a1a2e;margin:0 0 6px;font-weight:700}}
.intro{{font-size:12px;color:#666;margin:0 0 16px;line-height:1.7}}
table{{width:100%;border-collapse:collapse;font-size:12.5px}}
td{{padding:9px 0;vertical-align:top;border-bottom:1px solid #eee;line-height:1.7}}
td.k{{width:110px;color:#666}}
a{{overflow-wrap:anywhere;color:#2c2c2c;text-decoration:none}}
</style>
</head>
<body>
<div class="wrap">
  <h1>{t["heading"]}</h1>
  <p class="intro">{t["intro"]}</p>
  <table>
{items}
  </table>
</div>
</body>
</html>"""


def header_template(lang_key, chapter_title):
    site = build_mod.LANGUAGES[lang_key]["site_title"]
    return (
        f'<div style="width:100%;font-size:11pt;color:#555;'
        f'display:flex;justify-content:space-between;align-items:baseline;'
        f'padding:0 {MARGIN_LEFT}in;font-family:{FONT_FAMILY};">'
        f'<span>{site}</span>'
        f'<span>{chapter_title}</span>'
        f'</div>'
    )


def roman_num(n):
    """整数 → 罗马数字。"""
    vals = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    result = ""
    for v, sym in vals:
        while n >= v:
            result += sym
            n -= v
    return result


# ============================================================
#  页脚盖印（reportlab，合并后连续编号）
# ============================================================

def _stamp_engine():
    """惰性初始化 reportlab 字体。"""
    if getattr(_stamp_engine, "ready", False):
        return
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.cidfonts import UnicodeCIDFont
    # reportlab 将 MSung-Light（Adobe-CNS1 繁体字体）硬编码映射到简体
    # UniGB-UCS2-H CMap，繁体专用字形（如"頁"）在该 CMap 中无对应，
    # 页脚会渲染为空白；这里修正为 UniCNS-UCS2-H。
    from reportlab.pdfbase import _cidfontdata
    _cidfontdata.defaultUnicodeEncodings["MSung-Light"] = ("cht", "UniCNS-UCS2-H")
    pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
    pdfmetrics.registerFont(UnicodeCIDFont("MSung-Light"))
    _stamp_engine.ready = True


def make_footer_overlay(text, page_w, page_h, font_name):
    """生成一页页脚覆盖层（含指定文本）。"""
    import io
    from reportlab.pdfgen import canvas
    from pypdf import PdfReader

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(page_w, page_h))
    c.setFont(font_name, 11)
    c.setFillColorRGB(0.42, 0.42, 0.42)
    c.drawCentredString(page_w / 2, 0.42 * 72, text)
    c.save()
    buf.seek(0)
    return PdfReader(buf).pages[0]


def stamp_footer(pdf_path, lang_key):
    """为单个 PDF 的每一页盖印页脚（页码按该 PDF 自身计）。"""
    from pypdf import PdfReader, PdfWriter

    _stamp_engine()
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    total = len(reader.pages)
    template = FOOTER_TEXTS[lang_key]
    font_name = FOOTER_FONTS[lang_key]
    for i, page in enumerate(reader.pages, start=1):
        text = template.format(x=i, y=total)
        overlay = make_footer_overlay(
            text, float(page.mediabox.width), float(page.mediabox.height), font_name
        )
        page.merge_page(overlay, over=True)
        writer.add_page(page)
    tmp = pdf_path + ".tmp"
    with open(tmp, "wb") as f:
        writer.write(f)
    os.replace(tmp, pdf_path)


# ============================================================
#  Chrome DevTools Protocol 客户端
# ============================================================

try:
    import websocket
    import urllib.request
except ImportError:
    websocket = None
    urllib = None


class CDPClient:
    """最小化的 Chrome DevTools Protocol 客户端（仅打印所需）。"""

    def __init__(self, port):
        self.port = port
        self.ws = None
        self._id = 0

    def connect(self):
        targets = json.loads(
            urllib.request.urlopen(
                f"http://127.0.0.1:{self.port}/json", timeout=10
            ).read().decode()
        )
        page_targets = [t for t in targets if t.get("type") == "page"]
        if not page_targets:
            raise RuntimeError("未找到 Chrome 页面目标")
        self.ws = websocket.create_connection(
            page_targets[0]["webSocketDebuggerUrl"], timeout=30
        )

    def call(self, method, params=None):
        self._id += 1
        self.ws.send(json.dumps({
            "id": self._id, "method": method, "params": params or {}
        }))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == self._id:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})

    def navigate(self, url, settle=1.0):
        self.call("Page.enable")
        self.call("Page.navigate", {"url": url})
        deadline = time.time() + 20
        while time.time() < deadline:
            msg = json.loads(self.ws.recv())
            if msg.get("method") == "Page.loadEventFired":
                break
        # 触发懒加载图片 + 等待图片解码
        self.call("Runtime.evaluate", {
            "expression": "window.scrollTo(0, document.body.scrollHeight); "
                          "window.scrollTo(0, 0);"
        })
        time.sleep(settle)

    def print_to_pdf(self, out_path, header=None, footer=None,
                     margin_top=MARGIN_TOP, margin_bottom=MARGIN_BOTTOM,
                     margin_left=MARGIN_LEFT, margin_right=MARGIN_RIGHT):
        params = {
            "printBackground": True,
            "displayHeaderFooter": bool(header or footer),
            "headerTemplate": header or "<div></div>",
            "footerTemplate": footer or "<div></div>",
            "marginTop": margin_top,
            "marginBottom": margin_bottom,
            "marginLeft": margin_left,
            "marginRight": margin_right,
            "paperWidth": PAPER_W_IN,
            "paperHeight": PAPER_H_IN,
            "preferCSSPageSize": False,
            "transferMode": "ReturnAsBase64",
        }
        result = self.call("Page.printToPDF", params)
        with open(out_path, "wb") as f:
            f.write(base64.b64decode(result["data"]))

    def close(self):
        if self.ws:
            try:
                self.ws.close()
            except Exception:
                pass


def start_chrome(chrome):
    port = free_port()
    user_dir = tempfile.mkdtemp(prefix="ftc-pdf-")
    proc = subprocess.Popen(
        [chrome, "--headless=new", "--disable-gpu",
         f"--remote-debugging-port={port}",
         "--remote-allow-origins=*",
         f"--user-data-dir={user_dir}",
         "--no-first-run", "--no-default-browser-check",
         "--disable-extensions", "about:blank"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    deadline = time.time() + 15
    while time.time() < deadline:
        try:
            urllib.request.urlopen(
                f"http://127.0.0.1:{port}/json/version", timeout=1
            )
            return proc, port
        except Exception:
            time.sleep(0.2)
    proc.kill()
    raise RuntimeError("Chrome 调试端口启动超时")


def render_toc(lang_key, rows):
    """
    生成目录页 HTML。
    rows: [(标题, 级别(1|2), 页码标签)]，级别 2 缩进显示。
    """
    toc_title = TOC_TITLES[lang_key]
    row_html = []
    for title, level, label in rows:
        cls = "lvl1" if level == 1 else "lvl2"
        row_html.append(
            f'<div class="row {cls}"><span class="name">{title}</span>'
            f'<span class="pg">{label}</span></div>'
        )
    rows_str = "\n".join(row_html)
    return f"""<!DOCTYPE html>
<html lang="{lang_key}">
<head>
<meta charset="UTF-8">
<style>
html,body{{margin:0;padding:0}}
.toc{{
  width:100%;box-sizing:border-box;
  padding:0 0.45in;font-family:{FONT_FAMILY}
}}
.toc h1{{
  font-size:22pt;text-align:center;margin:0 0 30pt;padding-top:28pt;
  font-weight:700;color:#1a1a2e;line-height:1.4
}}
.toc .row{{
  display:flex;align-items:baseline;font-size:12.5pt;
  border-bottom:1px dotted #ccc;page-break-inside:avoid
}}
.toc .row.lvl1{{height:38pt;line-height:38pt;font-weight:600;color:#2c2c2c}}
.toc .row.lvl2{{height:34pt;line-height:34pt;padding-left:24pt;color:#444}}
.toc .row .pg{{margin-left:auto;color:#666;font-variant-numeric:tabular-nums}}
</style>
</head>
<body>
<div class="toc">
  <h1>{toc_title}</h1>
{rows_str}
</div>
</body>
</html>"""


# ============================================================
#  文本标准化与目录行定位
# ============================================================

def norm(text):
    """NFKC 归一化（PDF 字体子集产生的异体字形 → 标准字形）+ 去空格。"""
    import unicodedata
    return unicodedata.normalize("NFKC", text).replace(" ", "")


def _text_position(cm, tm):
    """
    将 pypdf 提供的 (cm, tm) 换算为页面标准坐标（y 自底向上）。

    Chrome 导出的正文流 cm≈[0.75,0,0,-0.75,90,769.92]（缩放+翻转+平移），
    字形级 tm 已含翻转（tm[3]=-1），故直接按
      x = cm[0]*tm[4] + cm[2]*tm[5] + cm[4]
      y = cm[1]*tm[4] + cm[3]*tm[5] + cm[5]
    计算（与像素渲染实测一致）。
    """
    x = cm[0] * tm[4] + cm[2] * tm[5] + cm[4]
    y = cm[1] * tm[4] + cm[3] * tm[5] + cm[5]
    return x, y


def extract_row_lines(page):
    """
    提取页面正文文本行，按视觉从上到下返回 [(页面y, 文本)]。

    pypdf 的 tm 是未变换坐标，必须用 cm 矩阵换算为页面坐标
    （y 自底向上）；页眉/页脚/盖印层换算后落在上下边距区，过滤之。
    """
    groups = {}
    page_h = float(page.mediabox.height)

    def visitor(text, cm, tm, font_dict, font_size):
        x, y = _text_position(cm, tm)
        if y < MARGIN_BOTTOM * 72 or y > page_h - MARGIN_TOP * 72:
            return
        key = int(round(y / 5.0))
        groups.setdefault(key, []).append((x, text))

    page.extract_text(visitor_text=visitor)
    lines = []
    for key in sorted(groups.keys(), reverse=True):
        parts = sorted(groups[key], key=lambda p: p[0])
        text = "".join(t for _, t in parts)
        lines.append((key * 5.0, norm(text)))
    return lines


def chapter_h2_pages(tmp_pdf, h2_count):
    """
    按字号检测各章 h2 标题所在页（不依赖文本匹配，
    规避 PDF 字体子集产生的异体字形问题）。
    实测 h2 打印字号 Tf = 24.0pt，检测范围 23.0–25.0pt。
    """
    from pypdf import PdfReader
    reader = PdfReader(tmp_pdf)
    lines_per_page = []
    for page in reader.pages:
        groups = {}
        page_h = float(page.mediabox.height)

        def visitor(text, cm, tm, font_dict, font_size):
            x, y = _text_position(cm, tm)
            if y < MARGIN_BOTTOM * 72 or y > page_h - MARGIN_TOP * 72:
                return
            key = int(round(y / 5.0))
            groups.setdefault(key, []).append(font_size)

        page.extract_text(visitor_text=visitor)
        n_h2 = 0
        for key in groups:
            sizes = groups[key]
            if any(23.0 < s < 25.0 for s in sizes):
                n_h2 += 1
        lines_per_page.append(n_h2)
    # 第 i 个 h2 所在页
    result = []
    for p, cnt in enumerate(lines_per_page):
        result.extend([p] * cnt)
    return result[:h2_count]


def merge_guide(cover_pdf, imprint_pdf, preface_pdf, toc_pdf, main_pdfs,
                resources_pdf, back_pdf, out_path, lang_key, toc_entries):
    """
    合并完整指南并盖印页脚：
    - 封面/封二（版权页）/封三（资源页）/封底不编号
    - 前言与目录用罗马数字（仅当前页码，无总页码），前言从 I 连续
    - 正文（队员须知起）用阿拉伯数字连续编号并标注总页数
    - toc_entries: [{title, level, dest}]，dest 为全书 0 基目标页；
      按实际渲染的文本行位置注入 PDF 内部超链接
    """
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import RectangleObject

    _stamp_engine()
    font_name = FOOTER_FONTS[lang_key]
    arabic_template = FOOTER_TEXTS[lang_key]

    writer = PdfWriter()

    def stamp(reader, text_fn):
        for page in reader.pages:
            text = text_fn()
            overlay = make_footer_overlay(
                text, float(page.mediabox.width), float(page.mediabox.height),
                font_name,
            )
            page.merge_page(overlay, over=True)
            writer.add_page(page)

    # 封面（不编号）
    writer.append(cover_pdf)

    # 封二（版权页，不编号）
    writer.append(imprint_pdf)

    # 前言：罗马数字，仅当前页码
    preface_reader = PdfReader(preface_pdf)
    roman_counter = 1

    def roman_text():
        nonlocal roman_counter
        label = roman_num(roman_counter)
        roman_counter += 1
        return label

    stamp(preface_reader, roman_text)

    # 目录：罗马数字继续
    toc_reader = PdfReader(toc_pdf)
    toc_start_index = len(writer.pages)
    stamp(toc_reader, roman_text)

    # 正文：阿拉伯数字连续编号 + 总页数
    total_main = sum(len(PdfReader(p).pages) for p in main_pdfs)
    page_no = 1

    def arabic_text():
        nonlocal page_no
        label = arabic_template.format(x=page_no, y=total_main)
        page_no += 1
        return label

    main_start_index = len(writer.pages)
    for p in main_pdfs:
        stamp(PdfReader(p), arabic_text)

    # 封三（资源与更新页，不编号）
    writer.append(resources_pdf)

    # 封底（不编号）
    writer.append(back_pdf)

    # 目录超链接：按实际文本行位置注入（跨页目录也能正确对齐）
    page_lines = []
    for p in range(toc_start_index, toc_start_index + len(toc_reader.pages)):
        page_lines.append(extract_row_lines(writer.pages[p]))
    # 第一页首行是"目录"大标题，去掉
    if page_lines and page_lines[0]:
        page_lines[0] = page_lines[0][1:]
    rows_global = []
    for pi, lines in enumerate(page_lines):
        rows_global.extend([(pi, y) for y, _ in lines])

    if len(rows_global) != len(toc_entries):
        print(f"  [警告] 目录行定位不一致: 提取到 {len(rows_global)} 行，"
              f"条目 {len(toc_entries)} 行（链接可能缺失/错位）")

    from pypdf.generic import (
        DictionaryObject, NameObject, ArrayObject, NumberObject,
    )
    page_w = PAPER_W_IN * 72
    x1 = MARGIN_LEFT * 72
    x2 = page_w - MARGIN_RIGHT * 72

    for idx, entry in enumerate(toc_entries):
        if entry["dest"] is None or idx >= len(rows_global):
            continue
        pi, y = rows_global[idx]
        row_h = 38.0 if entry["level"] == 1 else 34.0
        rect = RectangleObject([x1, y - 4.0, x2, y + row_h - 10.0])
        # 构造规范 /Dest（页面间接引用），pypdf 的 Link 注解在此场景
        # 会把 target_page_index 以纯数字写入，故手动构造
        ref = writer._add_object(writer.pages[entry["dest"]])
        annot = DictionaryObject()
        annot[NameObject("/Type")] = NameObject("/Annot")
        annot[NameObject("/Subtype")] = NameObject("/Link")
        annot[NameObject("/Rect")] = rect
        annot[NameObject("/Border")] = ArrayObject([
            NumberObject(0), NumberObject(0), NumberObject(0)
        ])
        annot[NameObject("/Dest")] = ArrayObject([
            ref, NameObject("/Fit")
        ])
        target_page = writer.pages[toc_start_index + pi]
        if target_page.annotations is None:
            target_page[NameObject("/Annots")] = ArrayObject()
        target_page.annotations.append(annot)

    with open(out_path, "wb") as f:
        writer.write(f)


def merge_pdfs(pdf_paths, output_path):
    """使用 pypdf 合并多个 PDF。"""
    from pypdf import PdfWriter
    writer = PdfWriter()
    for path in pdf_paths:
        writer.append(path)
    with open(output_path, "wb") as f:
        writer.write(f)


# ============================================================
#  导出主流程
# ============================================================

def export(lang_filter=None, page_filter=None):
    if websocket is None:
        print("[错误] 缺少 websocket-client 依赖，无法使用 CDP 打印。")
        print("       安装: pip3 install websocket-client")
        sys.exit(1)

    chrome = find_chrome()
    if not chrome:
        print("[错误] 未找到 Chrome/Edge 浏览器，无法导出 PDF。")
        print("       请安装 Google Chrome 或 Microsoft Edge 后重试。")
        sys.exit(1)

    print("=" * 56)
    print("  FTC 32477 Origin — PDF 导出工具（CDP）")
    print("=" * 56)
    print(f"  [使用] {chrome}")

    proc, port = start_chrome(chrome)
    client = CDPClient(port)
    try:
        client.connect()
        print(f"  [连接] 调试端口 {port}")

        langs = [lang_filter] if lang_filter else LANGUAGES
        pages = [page_filter] if page_filter else PAGE_KEYS

        tmp_dir = tempfile.mkdtemp(prefix="ftc-cover-")

        for lang in langs:
            if lang not in LANGUAGES:
                print(f"  [错误] 未知语言: {lang}")
                continue

            lang_pdf_dir = os.path.join(PDF_DIR, lang)
            os.makedirs(lang_pdf_dir, exist_ok=True)

            header_left = build_mod.LANGUAGES[lang]["site_title"]

            rendered = {}  # page_key -> 未盖印页脚的临时 PDF
            for page_key in pages:
                html_path = os.path.join(DIST_DIR, lang, f"{page_key}.html")
                if not os.path.exists(html_path):
                    print(f"  [跳过] {html_path} 不存在（请先运行 python3 build.py）")
                    continue
                chapter = build_mod.LANGUAGES[lang]["pages"][page_key]
                pdf_path = os.path.join(lang_pdf_dir, f"{page_key}.pdf")
                tmp_pdf = os.path.join(tmp_dir, f"{lang}-{page_key}.pdf")
                try:
                    # 渲染正文（仅页眉），临时文件供合并用
                    client.navigate("file://" + html_path)
                    client.print_to_pdf(
                        tmp_pdf,
                        header=header_template(lang, chapter),
                    )
                    # 单页 PDF：复制后按自身页数盖印页脚
                    shutil.copyfile(tmp_pdf, pdf_path)
                    stamp_footer(pdf_path, lang)
                    rendered[page_key] = tmp_pdf
                    print(f"  [生成] pdf/{lang}/{page_key}.pdf（页眉: {chapter}）")
                except Exception as e:
                    print(f"  [失败] {page_key}: {e}")

            # 完整指南：封面 + 封二(版权页) + 前言(罗马) + 目录(罗马) + 正文(阿拉伯) + 封三(资源页) + 封底
            merged_ok = False
            if set(PAGE_KEYS).issubset(rendered) and not page_filter:
                cover_html = os.path.join(tmp_dir, f"cover-{lang}.html")
                back_html = os.path.join(tmp_dir, f"back-{lang}.html")
                imprint_html = os.path.join(tmp_dir, f"imprint-{lang}.html")
                resources_html = os.path.join(tmp_dir, f"resources-{lang}.html")
                toc_html = os.path.join(tmp_dir, f"toc-{lang}.html")
                cover_pdf = os.path.join(tmp_dir, f"cover-{lang}.pdf")
                back_pdf = os.path.join(tmp_dir, f"back-{lang}.pdf")
                imprint_pdf = os.path.join(tmp_dir, f"imprint-{lang}.pdf")
                resources_pdf = os.path.join(tmp_dir, f"resources-{lang}.pdf")
                toc_pdf = os.path.join(tmp_dir, f"toc-{lang}.pdf")
                with open(cover_html, "w", encoding="utf-8") as f:
                    f.write(render_cover(lang))
                with open(back_html, "w", encoding="utf-8") as f:
                    f.write(render_back(lang))
                with open(imprint_html, "w", encoding="utf-8") as f:
                    f.write(render_imprint(lang))
                with open(resources_html, "w", encoding="utf-8") as f:
                    f.write(render_resources(lang))
                try:
                    client.navigate("file://" + cover_html)
                    client.print_to_pdf(cover_pdf, margin_top=0, margin_bottom=0,
                                        margin_left=0, margin_right=0)
                    client.navigate("file://" + back_html)
                    client.print_to_pdf(back_pdf, margin_top=0, margin_bottom=0,
                                        margin_left=0, margin_right=0)
                    client.navigate("file://" + imprint_html)
                    client.print_to_pdf(imprint_pdf, margin_top=0, margin_bottom=0,
                                        margin_left=0, margin_right=0)
                    client.navigate("file://" + resources_html)
                    client.print_to_pdf(resources_pdf)

                    # 计算正文各章起始页码（队员须知 = 第 1 页）
                    from pypdf import PdfReader as _R
                    main_keys = [k for k in PAGE_KEYS if k != "preface"]
                    page_counts = {k: len(_R(rendered[k]).pages) for k in main_keys}
                    starts = {}
                    acc = 1
                    for k in main_keys:
                        starts[k] = acc
                        acc += page_counts[k]

                    # 解析各章 h2 小标题及其章内页偏移（按字号定位，无文本匹配）
                    def h2_rows(k):
                        md_path = os.path.join(
                            build_mod.SRC_DIR, lang, f"{k}.md"
                        )
                        with open(md_path, encoding="utf-8") as f:
                            _, headings = build_mod.parse_markdown(f.read())
                        h2s = [h for h in headings if h["level"] == 2]
                        pages = chapter_h2_pages(rendered[k], len(h2s))
                        rows = []
                        for idx, h in enumerate(h2s):
                            local = pages[idx] if idx < len(pages) else 0
                            rows.append((h["text"], local))
                        return rows

                    # 目录行（标题, 级别, 页码标签）
                    preface_title = build_mod.LANGUAGES[lang]["pages"]["preface"]
                    toc_rows = [(preface_title, 1, roman_num(1))]
                    for k in main_keys:
                        title = build_mod.LANGUAGES[lang]["pages"][k]
                        toc_rows.append((title, 1, str(starts[k])))
                        for h2_title, local_off in h2_rows(k):
                            toc_rows.append(
                                (h2_title, 2, str(starts[k] + local_off))
                            )

                    with open(toc_html, "w", encoding="utf-8") as f:
                        f.write(render_toc(lang, toc_rows))
                    client.navigate("file://" + toc_html)
                    client.print_to_pdf(
                        toc_pdf,
                        header=header_template(lang, TOC_TITLES[lang]),
                    )

                    # 目标页（全书 0 基）：封面=0，封二=1，前言=2…
                    preface_pages = len(_R(rendered["preface"]).pages)
                    toc_pages = len(_R(toc_pdf).pages)
                    base = 2 + preface_pages + toc_pages

                    toc_entries = [
                        {"title": preface_title, "level": 1, "dest": 2}
                    ]
                    for k in main_keys:
                        title = build_mod.LANGUAGES[lang]["pages"][k]
                        toc_entries.append({
                            "title": title, "level": 1,
                            "dest": base + starts[k] - 1,
                        })
                        for h2_title, local_off in h2_rows(k):
                            toc_entries.append({
                                "title": h2_title, "level": 2,
                                "dest": base + starts[k] - 1 + local_off,
                            })

                    merged_path = os.path.join(
                        PDF_DIR,
                        f"FTC-Team-32477-Origin-Quick-Start-Guide-{build_mod.RELEASE_TAG}-{lang}.pdf",
                    )
                    merge_guide(
                        cover_pdf, imprint_pdf, rendered["preface"], toc_pdf,
                        [rendered[k] for k in main_keys], resources_pdf, back_pdf,
                        merged_path, lang, toc_entries,
                    )
                    merged_ok = True
                    size_kb = os.path.getsize(merged_path) / 1024
                    print(f"  [合并] FTC-Team-32477-Origin-Quick-Start-Guide-{build_mod.RELEASE_TAG}-{lang}.pdf "
                          f"（封面 + 封二 + 前言 + 目录（{len(toc_entries)} 行）"
                          f" + {len(main_keys)} 章 + 封三 + 封底，{size_kb:.0f} KB）")
                except Exception as e:
                    print(f"  [失败] 封面/目录/封底: {e}")

            # 单页 PDF 仅作调试用（--page）；完整导出合并成功后删除，只保留合并版
            if not page_filter and merged_ok:
                shutil.rmtree(lang_pdf_dir, ignore_errors=True)
                print(f"  [清理] 已删除单页 PDF 目录 pdf/{lang}/（仅保留合并版）")

        shutil.rmtree(tmp_dir, ignore_errors=True)
    finally:
        client.close()
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except Exception:
            proc.kill()

    print("-" * 56)
    print(f"  导出完成! 输出目录: {os.path.relpath(PDF_DIR, BASE_DIR)}")
    print("=" * 56)


if __name__ == "__main__":
    args = sys.argv[1:]
    lang_filter = None
    page_filter = None
    rebuild = False

    i = 0
    while i < len(args):
        if args[i] == "--lang" and i + 1 < len(args):
            lang_filter = args[i + 1]
            i += 2
        elif args[i] == "--page" and i + 1 < len(args):
            page_filter = args[i + 1]
            i += 2
        elif args[i] == "--rebuild":
            rebuild = True
            i += 1
        else:
            print(f"未知参数: {args[i]}")
            sys.exit(1)

    if rebuild:
        print("[准备] 先重新构建 HTML...")
        subprocess.run([sys.executable, os.path.join(BASE_DIR, "build.py")])

    export(lang_filter=lang_filter, page_filter=page_filter)
