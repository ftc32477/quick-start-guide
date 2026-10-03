#!/usr/bin/env python3
"""
FTC 32477 Origin 快速入门指南 — PDF 导出工具

基于 Chrome DevTools Protocol (CDP) 将 dist/ 中的 HTML 页面渲染为 PDF。
按教科书装订方式（封面/封底单独印刷，不印封二封三），页面顺序：
- 封面（队徽、队名、版本日期）
- 扉页（内页第 1 页，白底黑字复述封面信息）
- 版权页（扉页背面：完整书名、版次、版本号、发布日期、编写人员、法律声明）
- 页眉（"FTC 32477 Origin 快速入门指南" + 当前章回，reportlab 盖印）
- 页脚（居中"— X —"式页码，reportlab 盖印）
- 资源页（内页最后一页：在线版本、历史版本、开源仓库、意见反馈链接）
- 封底（居中队徽 + 右下角版本日期）
- 全部内容随语言自动本地化

用法:
    python3 build_pdf.py            # 导出所有语言的单页 PDF + 合并 PDF
    python3 build_pdf.py --lang en-us  # 仅导出指定语言（zh-hans / zh-hant / en-us / fr / es / ko）
    python3 build_pdf.py --page member  # 仅导出指定页面（仅单页，不含封面封底）
    python3 build_pdf.py --rebuild  # 先执行 build.py 再导出

输出:
    dist/pdf/FTC-Team-32477-Origin-Quick-Start-Guide-{RELEASE_TAG}-{lang}.pdf  — 完整指南 PDF（封面 + 扉页 + 版权页 + 正文 + 资源页 + 封底），
        dist/pdf/ 不入库（.gitignore），仅供本地自查纠错；正式发布版上传为 GitHub Release 资产，
        线上各语言主页的下载按钮指向 Release 资产链接

说明:
    - PDF 使用 fonts/subsets/ 中的开源字体子集（思源宋体/黑体、霞鹜文楷、
      Tinos；build 前自动校验用字覆盖，缺字报错并提示重建子集）
    - 单页 PDF（dist/pdf/{lang}/{page}.pdf，含页眉页脚）仅通过 --page 参数
      生成，用于内容调试；完整导出（不带 --page）在合并成功后会自动删除
      单页 PDF 目录，dist/pdf/ 下只保留六语言合并版指南。

依赖:
    - Google Chrome / Edge（无头模式 + 远程调试端口）
    - websocket-client（CDP 通信）: pip3 install websocket-client
    - pypdf（PDF 合并）: pip3 install pypdf
"""

import os
import re
import sys
import html
import time
import json
import base64
import socket
import shutil
import tempfile
import subprocess
import pathlib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_DIR = os.path.join(BASE_DIR, "dist")
PDF_DIR = os.path.join(DIST_DIR, "pdf")
IMAGES_DIR = os.path.join(BASE_DIR, "images")

sys.path.insert(0, BASE_DIR)
import build as build_mod  # noqa: E402  复用 LANGUAGES / PAGE_KEYS / VERSIONS / LANG_HOME_TEXTS / format_release_date / RELEASE_TAG

PAGE_KEYS = build_mod.PAGE_KEYS
LANGUAGES = list(build_mod.LANGUAGES.keys())

CHROME_CANDIDATES = [
    "/Applications/Google Chrome Dev.app/Contents/MacOS/Google Chrome Dev",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge Dev.app/Contents/MacOS/Microsoft Edge Dev",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
]

# 封面/封底的本地化文案
PDF_TEXTS = {
    "zh-hans": {
        "badge": "TEAM 32477 ORIGIN",
        "title": "FIRST\u00ae Tech Challenge",
        "name": "32477 Origin \u5feb\u901f\u5165\u95e8\u6307\u5357",
        "name2": "Quick Start Guide",
        "school": "\u5317\u4eac\u5341\u4e00\u5b9e\u9a8c\u4e2d\u5b66",
        "lang": "\u7b80\u4f53\u4e2d\u6587\u7248",
    },
    "zh-hant": {
        "name": "32477 Origin \u5feb\u901f\u5165\u95e8\u6307\u5357",
        "school": "\u5317\u4eac\u5341\u4e00\u5be6\u9a57\u4e2d\u5b78",
        "lang": "\u7e41\u9ad4\u4e2d\u6587\u7248",
    },
    "en-us": {
        "name": "32477 Origin Quick Start Guide",
        "name2": "\u5feb\u901f\u5165\u95e8\u6307\u5357",
        "school": "Beijing National Day Experimental School",
        "lang": "English (US) Edition",
    },
    "fr": {
        "name": "32477 Origin Guide de d\u00e9marrage rapide",
        "name2": "\u5feb\u901f\u5165\u95e8\u6307\u5357",
        "school": "Beijing National Day Experimental School",
        "lang": "\u00c9dition fran\u00e7aise",
    },
    "es": {
        "name": "Gu\u00eda de inicio r\u00e1pido de 32477 Origin",
        "name2": "\u5feb\u901f\u5165\u95e8\u6307\u5357",
        "school": "Beijing National Day Experimental School",
        "lang": "Edici\u00f3n en espa\u00f1ol",
    },
    "ko": {
        "name": "32477 Origin \ube60\ub978 \uc2dc\uc791 \uac00\uc774\ub4dc",
        "name2": "\u5feb\u901f\u5165\u95e8\u6307\u5357",
        "school": "Beijing National Day Experimental School",
        "lang": "\ud55c\uad6d\uc5b4\ud310",
    },
}

# 目录标题本地化
TOC_TITLES = {
    "zh-hans": "\u76ee\u5f55",
    "zh-hant": "\u76ee\u9304",
    "en-us": "Table of Contents",
    "fr": "Table des mati\u00e8res",
    "es": "\u00cdndice",
    "ko": "\ubaa9\ucc28",
}

# 页脚文案（reportlab 盖印，x=当前页）与字体（内置 CID 字体）
FOOTER_TEXTS = {
    "zh-hans": "\u2014 {x} \u2014",
    "zh-hant": "\u2014 {x} \u2014",
    "en-us": "\u2014 {x} \u2014",
    "fr": "\u2014 {x} \u2014",
    "es": "\u2014 {x} \u2014",
    "ko": "\u2014 {x} \u2014",
}
# ============================================================
#  字体（PDF 专用；网页版仍用系统字体）
# ============================================================
# 开源字体按各语言实际用字裁成子集（fonts/subsets/，入库），
# 由 fonts/build_subsets.py 生成（详见 README「PDF 字体」章节）；
# 网页版与打印 HTML 不使用。
# 选型：正文宋体/明体（思源宋体）、标题黑体（思源黑体）、
# 引文/图注/前言楷体（霞鹜文楷，子集改名 Origin Kai）、
# 西文与数字 Times New Roman（缺失时 Tinos，度量兼容）。
FONTS_SUBSET_DIR = os.path.join(BASE_DIR, "fonts", "subsets")

# (字体族, 样式, 字重, 子集文件名)
FONT_FACES = [
    ("Tinos", "normal", 400, "Tinos-Regular.ttf"),
    ("Tinos", "normal", 700, "Tinos-Bold.ttf"),
    ("Tinos", "italic", 400, "Tinos-Italic.ttf"),
    ("Tinos", "italic", 700, "Tinos-BoldItalic.ttf"),
    ("Noto Serif SC", "normal", 400, "NotoSerifSC-Regular.ttf"),
    ("Noto Serif SC", "normal", 700, "NotoSerifSC-Bold.ttf"),
    ("Noto Serif TC", "normal", 400, "NotoSerifTC-Regular.ttf"),
    ("Noto Serif TC", "normal", 700, "NotoSerifTC-Bold.ttf"),
    ("Noto Sans SC", "normal", 400, "NotoSansSC-Regular.ttf"),
    ("Noto Sans SC", "normal", 700, "NotoSansSC-Bold.ttf"),
    ("Noto Sans TC", "normal", 400, "NotoSansTC-Regular.ttf"),
    ("Noto Sans TC", "normal", 700, "NotoSansTC-Bold.ttf"),
    ("Noto Serif KR", "normal", 400, "NotoSerifKR-Regular.ttf"),
    ("Noto Serif KR", "normal", 700, "NotoSerifKR-Bold.ttf"),
    ("Noto Sans KR", "normal", 400, "NotoSansKR-Regular.ttf"),
    ("Noto Sans KR", "normal", 700, "NotoSansKR-Bold.ttf"),
    ("Noto Sans", "normal", 400, "NotoSans-Regular.ttf"),
    ("Noto Sans", "normal", 700, "NotoSans-Bold.ttf"),
    ("Origin Kai SC", "normal", 400, "OriginKaiSC-Regular.ttf"),
    ("Origin Kai SC", "normal", 700, "OriginKaiSC-Bold.ttf"),
    ("Origin Kai TC", "normal", 400, "OriginKaiTC-Regular.ttf"),
    ("Origin Kai TC", "normal", 700, "OriginKaiTC-Bold.ttf"),
]

# 各语言的角色字体栈：正文（宋体/Tinos）、标题（黑体）、楷体（引文/图注/前言）
# 注：繁体/韩语字体不含全部简体专用字（如「谢」「简」），故在栈尾
# 追加思源宋体/黑体简体作兜底，确保文档内简体注记不缺字。
BODY_FONTS = {
    "zh-hans": "'Times New Roman','Tinos','Noto Serif SC',serif",
    "zh-hant": "'Times New Roman','Tinos','Noto Serif TC','Noto Serif SC',serif",
    "en-us": "'Times New Roman','Tinos','Noto Serif SC',serif",
    "fr": "'Times New Roman','Tinos','Noto Serif SC',serif",
    "es": "'Times New Roman','Tinos','Noto Serif SC',serif",
    "ko": "'Times New Roman','Tinos','Noto Serif KR','Noto Serif SC',serif",
}
HEAD_FONTS = {
    "zh-hans": "'Noto Sans SC','Noto Sans',sans-serif",
    "zh-hant": "'Noto Sans TC','Noto Sans','Noto Sans SC',sans-serif",
    "en-us": "'Noto Sans','Noto Sans SC',sans-serif",
    "fr": "'Noto Sans','Noto Sans SC',sans-serif",
    "es": "'Noto Sans','Noto Sans SC',sans-serif",
    "ko": "'Noto Sans KR','Noto Sans','Noto Sans SC',sans-serif",
}
KAI_FONTS = {
    "zh-hans": "'Origin Kai SC','Noto Serif SC',serif",
    "zh-hant": "'Origin Kai TC','Noto Serif TC','Noto Serif SC',serif",
    "en-us": BODY_FONTS["en-us"],
    "fr": BODY_FONTS["fr"],
    "es": BODY_FONTS["es"],
    "ko": BODY_FONTS["ko"],
}
MONO_FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

# 页眉/页脚盖印字体（reportlab 直接嵌入子集 TTF）
STAMP_FONTS = {
    "zh-hans": ("NotoSerifSC", "NotoSerifSC-Regular.ttf"),
    "zh-hant": ("NotoSerifTC", "NotoSerifTC-Regular.ttf"),
    "en-us": ("Tinos", "Tinos-Regular.ttf"),
    "fr": ("Tinos", "Tinos-Regular.ttf"),
    "es": ("Tinos", "Tinos-Regular.ttf"),
    "ko": ("NotoSerifKR", "NotoSerifKR-Regular.ttf"),
}

# 纸张与页边距：A4（210×297mm），上下 2.54cm，左右 3.18cm
PAPER_W_IN = 8.27   # 210mm
PAPER_H_IN = 11.69  # 297mm
MARGIN_TOP = 1.0       # 2.54cm
MARGIN_BOTTOM = 1.0    # 2.54cm
MARGIN_LEFT = 1.25     # 3.18cm
MARGIN_RIGHT = 1.25    # 3.18cm


# ============================================================
#  字体子集加载 / 注入 / 用字覆盖校验
# ============================================================

_font_faces_css_cache = None


def font_faces_css():
    """全部 @font-face 规则（file:// 指向 fonts/subsets/，仅 PDF 构建使用）。"""
    global _font_faces_css_cache
    if _font_faces_css_cache is None:
        rules = []
        for family, style, weight, fname in FONT_FACES:
            path = os.path.join(FONTS_SUBSET_DIR, fname)
            if not os.path.exists(path):
                continue
            uri = pathlib.Path(path).resolve().as_uri()
            rules.append(
                f"@font-face{{font-family:'{family}';font-style:{style};"
                f"font-weight:{weight};src:url('{uri}') format('truetype');}}"
            )
        _font_faces_css_cache = "\n".join(rules)
    return _font_faces_css_cache


def pdf_role_css(lang_key, page_key=None):
    """按角色指定字体：正文 / 标题 / 楷体（引文、图注、前言）。"""
    body = BODY_FONTS[lang_key]
    head = HEAD_FONTS[lang_key]
    kai = KAI_FONTS[lang_key]
    css = (
        f"body,main,p,li,td,th,table{{font-family:{body};}}"
        f"h1,h2,h3,h4,h5,h6{{font-family:{head};}}"
        f"blockquote,blockquote p,blockquote li{{font-family:{kai};}}"
        f"figcaption,.img-row figcaption{{font-family:{kai};}}"
        f"pre,code,kbd,samp{{font-family:{MONO_FONT};}}"
    )
    if page_key == "preface" and lang_key in ("zh-hans", "zh-hant"):
        css += f"main p{{font-family:{kai};}}"
    return css


def wait_fonts(client):
    """等待页面字体加载完成（避免打印时回退到系统字体）。"""
    client.call("Runtime.evaluate", {
        "expression": "document.fonts.ready.then(() => document.fonts.status)",
        "awaitPromise": True, "returnByValue": True,
    })


def inject_pdf_fonts(client, lang_key, page_key):
    """把 @font-face 与角色字体注入已打开的页面，并等待字体加载完成。"""
    css = font_faces_css() + "\n" + pdf_role_css(lang_key, page_key)
    expr = (
        "(() => {"
        f"const css = {json.dumps(css)};"
        "let s = document.getElementById('pdf-fonts');"
        "if (!s) { s = document.createElement('style'); s.id = 'pdf-fonts';"
        "document.head.appendChild(s); }"
        "s.textContent = css;"
        "return true;"
        "})()"
    )
    client.call("Runtime.evaluate", {"expression": expr, "returnByValue": True})
    wait_fonts(client)


def _iter_strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from _iter_strings(v)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            yield from _iter_strings(v)


def required_text(lang_key):
    """该语言 PDF 中出现的全部文本（.md 源 + 构建模板文案），用于覆盖校验。"""
    parts = []
    md_dir = os.path.join(build_mod.SRC_DIR, lang_key)
    if os.path.isdir(md_dir):
        for name in sorted(os.listdir(md_dir)):
            if name.endswith(".md"):
                with open(os.path.join(md_dir, name), encoding="utf-8") as f:
                    parts.append(f.read())
    for obj in (
        build_mod.LANGUAGES[lang_key],
        build_mod.LANG_HOME_TEXTS.get(lang_key, {}),
        PDF_TEXTS.get(lang_key, {}),
        TOC_TITLES.get(lang_key, ""),
        FOOTER_TEXTS.get(lang_key, ""),
        IMPRINT_TEXTS.get(lang_key, {}),
        RESOURCE_TEXTS.get(lang_key, {}),
    ):
        parts.append("".join(_iter_strings(obj)))
    # 历史版本页（网页）用的 changes 字段不进 PDF，故不计入用字
    for v in build_mod.VERSIONS:
        parts.append("".join(_iter_strings(v.get("name", {}).get(lang_key, ""))))
        parts.append("".join(_iter_strings(v.get("pdfs", {}).get(lang_key, ""))))
    return "".join(parts)


def used_font_families(lang_key):
    stacks = BODY_FONTS[lang_key] + HEAD_FONTS[lang_key] + KAI_FONTS[lang_key]
    return set(re.findall(r"'([^']+)'", stacks))


_coverage_cache = None


def _load_coverage():
    global _coverage_cache
    if _coverage_cache is None:
        path = os.path.join(FONTS_SUBSET_DIR, "coverage.json")
        if not os.path.exists(path):
            _coverage_cache = {}
        else:
            with open(path, encoding="utf-8") as f:
                _coverage_cache = json.load(f)
    return _coverage_cache


def _checkable(ch):
    import unicodedata
    return unicodedata.category(ch)[0] != "C"


def check_font_coverage(lang_key):
    """构建前校验：该语言 PDF 全部用字都在其字体栈子集覆盖范围内。"""
    coverage = _load_coverage()
    covered = set()
    for family, _style, _weight, fname in FONT_FACES:
        if family not in used_font_families(lang_key):
            continue
        for start, end in coverage.get(fname, []):
            covered.update(range(start, end + 1))
    missing = sorted({
        ch for ch in required_text(lang_key)
        if _checkable(ch) and ord(ch) not in covered
    })
    if missing:
        sample = " ".join(f"{ch}(U+{ord(ch):04X})" for ch in missing[:20])
        more = " …" if len(missing) > 20 else ""
        print(f"  [错误] {lang_key} PDF 用字超出字体子集覆盖（共 {len(missing)} 字）：")
        print(f"         {sample}{more}")
        print("         请运行 python3 fonts/build_subsets.py 重新生成字体子集后重试"
              "（需 pip3 install fonttools）。")
        sys.exit(1)


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
    t["date"] = build_mod.latest_edition(lang_key)
    logo_path = "file://" + os.path.join(IMAGES_DIR, "basic", "team_logo.png")
    head = HEAD_FONTS[lang_key]
    font_css = font_faces_css()
    return f"""<!DOCTYPE html>
<html lang="{lang_key}">
<head>
<meta charset="UTF-8">
<style>
{font_css}
@page {{ size: A4; margin: 0; }}
html,body{{margin:0;padding:0}}
.cover{{
  width:100%;height:100vh;overflow:hidden;
  background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  color:#fff;font-family:{head};position:relative;text-align:center
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
  position:absolute;bottom:48px;left:0;right:0;
  font-size:16px;opacity:.8;letter-spacing:2px;line-height:2
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
  <div class="date">{t["lang"]}<br>{t["date"]}</div>
</div>
</body>
</html>"""


def render_title_page(lang_key):
    """扉页（内页第 1 页，白底黑字）：按教科书方式复述封面信息。"""
    t = dict(PDF_TEXTS["zh-hans"])
    t.update(PDF_TEXTS[lang_key])
    t["date"] = build_mod.latest_edition(lang_key)
    logo_path = "file://" + os.path.join(IMAGES_DIR, "basic", "team_logo.png")
    head = HEAD_FONTS[lang_key]
    body = BODY_FONTS[lang_key]
    font_css = font_faces_css()
    return f"""<!DOCTYPE html>
<html lang="{lang_key}">
<head>
<meta charset="UTF-8">
<style>
{font_css}
@page {{ size: A4; margin: 0; }}
html,body{{margin:0;padding:0}}
.wrap{{
  width:100vw;height:100vh;box-sizing:border-box;padding:1in 1.25in;
  font-family:{body};color:#1a1a2e;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  text-align:center;position:relative
}}
/* 与封面一致：内容整体上移，集群中心位于黄金分割点（38.2vh） */
.wrap .inner{{
  position:relative;display:flex;flex-direction:column;align-items:center;
  transform:translateY(-11.8vh)
}}
.wrap img.logo{{width:110px;height:110px;border-radius:24px;margin-bottom:28px}}
.badge{{
  font-family:{head};font-size:13px;font-weight:600;letter-spacing:3px;
  border:1.5px solid #1a1a2e;border-radius:18px;padding:4px 18px;margin-bottom:30px
}}
h1{{font-family:{head};font-size:26px;font-weight:700;margin:0 0 16px}}
.name{{font-family:{head};font-size:30px;font-weight:700;margin-bottom:14px}}
.name2{{font-size:16px;color:#444;margin-bottom:36px}}
.school{{font-size:15px;color:#444}}
.date{{
  position:absolute;bottom:1in;left:0;right:0;
  font-size:14px;color:#444;line-height:2
}}
</style>
</head>
<body>
<div class="wrap">
  <div class="inner">
    <img class="logo" src="{logo_path}">
    <div class="badge">{t["badge"]}</div>
    <h1>{t["title"]}</h1>
    <div class="name">{t["name"]}</div>
    <div class="name2">{t["name2"]}</div>
    <div class="school">{t["school"]}</div>
  </div>
  <div class="date">{t["lang"]}<br>{t["date"]}</div>
</div>
</body>
</html>"""


def render_back(lang_key):
    t = dict(PDF_TEXTS["zh-hans"])
    t.update(PDF_TEXTS[lang_key])
    t["date"] = build_mod.latest_edition(lang_key)
    logo_path = "file://" + os.path.join(IMAGES_DIR, "basic", "team_logo.png")
    head = HEAD_FONTS[lang_key]
    font_css = font_faces_css()
    return f"""<!DOCTYPE html>
<html lang="{lang_key}">
<head>
<meta charset="UTF-8">
<style>
{font_css}
@page {{ size: A4; margin: 0; }}
html,body{{margin:0;padding:0}}
/* 封底与封面镜像对称：渐变方向翻转、光斑位置镜像 */
.back{{
  width:100%;height:100vh;overflow:hidden;
  background:linear-gradient(45deg,#1a1a2e 0%,#16213e 100%);
  display:flex;align-items:center;justify-content:center;
  font-family:{head};position:relative
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
  position:absolute;bottom:48px;right:56px;font-size:15px;color:#c9c9d4;letter-spacing:2px;
  text-align:right;line-height:2
}}
</style>
</head>
<body>
<div class="back">
  <div class="glow"></div>
  <img class="logo" src="{logo_path}">
  <div class="date">{t["lang"]}<br>{t["date"]}</div>
</div>
</body>
</html>"""


# 版权页（扉页背面）与资源更新页（内页最后一页）文案
IMPRINT_TEXTS = {
    "zh-hans": {
        "title_label": "\u4e66\u540d",
        "fields": [
            ("\u7248\u6b21", "{edition}"),
            ("\u7248\u672c\u53f7", "{tag}"),
            ("\u53d1\u5e03\u65e5\u671f", "{date}"),
            ("\u8bed\u8a00\u7248\u672c", "{lang_edition}"),
            ("\u4e3b\u7f16", "\u4ed8\u4fee\u9f50"),
            ("\u7f16\u5199\u4eba\u5458", "\u675c\u661f\u6d32\u3001\u8c22\u91d1\u707f \u7b49"),
            ("\u51fa\u54c1", "FTC 32477 Origin \u00b7 \u5317\u4eac\u5341\u4e00\u5b9e\u9a8c\u4e2d\u5b66"),
            ("\u5730\u5740", "\u5317\u4eac\u5e02\u6d77\u6dc0\u533a\u592a\u5e73\u8def8\u53f7 \u00b7 \u90ae\u653f\u7f16\u7801 100039"),
        ],
    },
    "zh-hant": {
        "title_label": "\u66f8\u540d",
        "fields": [
            ("\u7248\u6b21", "{edition}"),
            ("\u7248\u672c\u865f", "{tag}"),
            ("\u767c\u5e03\u65e5\u671f", "{date}"),
            ("\u8a9e\u8a00\u7248\u672c", "{lang_edition}"),
            ("\u4e3b\u7de8", "\u4ed8\u4fee\u9f4a\uff08\u4ed8\u4fee\u9f50\uff09"),
            ("\u7de8\u5beb\u4eba\u54e1", "\u675c\u661f\u6d32\u3001\u8b1d\u91d1\u71e6\uff08\u8c22\u91d1\u707f\uff09 \u7b49"),
            ("\u51fa\u54c1", "FTC 32477 Origin \u00b7 \u5317\u4eac\u5341\u4e00\u5be6\u9a57\u4e2d\u5b78"),
            ("\u5730\u5740", "\u5317\u4eac\u5e02\u6d77\u6dc0\u5340\u592a\u5e73\u8def8\u865f \u00b7 \u90f5\u901e\u5340\u865f 100039"),
        ],
    },
    "en-us": {
        "title_label": "Title",
        "fields": [
            ("Edition", "{edition}"),
            ("Version", "{tag}"),
            ("Release Date", "{date}"),
            ("Language Edition", "{lang_edition}"),
            ("Chief Editor", "Fu Xiuqi (\u4ed8\u4fee\u9f50)"),
            ("Writers", "Du Xingzhou (\u675c\u661f\u6d32), Xie Jincan (\u8c22\u91d1\u707f), et al."),
            ("Produced by", "FTC 32477 Origin \u00b7 Beijing National Day Experimental School"),
            ("Address", "No. 8 Taiping Road, Haidian District, Beijing 100039, China"),
        ],
    },
    "fr": {
        "title_label": "Titre",
        "fields": [
            ("\u00c9dition", "{edition}"),
            ("Version", "{tag}"),
            ("Date de publication", "{date}"),
            ("\u00c9dition linguistique", "{lang_edition}"),
            ("R\u00e9dacteur en chef", "Fu Xiuqi (\u4ed8\u4fee\u9f50)"),
            ("R\u00e9dacteurs", "Du Xingzhou (\u675c\u661f\u6d32), Xie Jincan (\u8c22\u91d1\u707f), et al."),
            ("Produit par", "FTC 32477 Origin \u00b7 Beijing National Day Experimental School"),
            ("Adresse", "N\u00b0 8 Taiping Road, district de Haidian, P\u00e9kin 100039, Chine"),
        ],
    },
    "es": {
        "title_label": "T\u00edtulo",
        "fields": [
            ("Edici\u00f3n", "{edition}"),
            ("Versi\u00f3n", "{tag}"),
            ("Fecha de publicaci\u00f3n", "{date}"),
            ("Edici\u00f3n ling\u00fc\u00edstica", "{lang_edition}"),
            ("Redactor jefe", "Fu Xiuqi (\u4ed8\u4fee\u9f50)"),
            ("Redactores", "Du Xingzhou (\u675c\u661f\u6d32), Xie Jincan (\u8c22\u91d1\u707f), et al."),
            ("Producido por", "FTC 32477 Origin \u00b7 Beijing National Day Experimental School"),
            ("Direcci\u00f3n", "N.\u00ba 8 Taiping Road, distrito de Haidian, Pek\u00edn 100039, China"),
        ],
    },
    "ko": {
        "title_label": "\uc81c\ubaa9",
        "fields": [
            ("\ud310\ubcf8", "{edition}"),
            ("\ubc84\uc804", "{tag}"),
            ("\ucd9c\uc2dc\uc77c", "{date}"),
            ("\uc5b8\uc5b4\ud310", "{lang_edition}"),
            ("\ud3b8\uc9d1\uc7a5", "\ubd80\uc218\uc81c(\u4ed8\u4fee\u9f50)"),
            ("\uc9d1\ud544\uc9c4", "\ub450\uc131\uc8fc(\u675c\u661f\u6d32), \uc0ac\uae08\ucc2c(\u8c22\u91d1\u707f) \ub4f1"),
            ("\uc81c\uc791", "FTC 32477 Origin \u00b7 Beijing National Day Experimental School"),
            ("\uc8fc\uc18c", "\uc911\uad6d \ubca0\uc774\uc9d5\uc2dc \ud558\uc774\ub518\uad6c \ud0c0\uc774\ud551\ub85c 8\ubc88\uc9c0, \uc6b0\ud3b8\ubc88\ud638 100039"),
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
    "es": {
        "heading": "Recursos y actualizaciones",
        "intro": "Esta gu\u00eda se revisa de forma continua. Obtenga los contenidos m\u00e1s recientes a trav\u00e9s de los siguientes canales:",
        "items": [
            ("Edici\u00f3n en l\u00ednea", "https://ftc32477.github.io/docs/"),
            ("Historial de versiones", "https://ftc32477.github.io/docs/{lang}/versions.html"),
            ("Repositorio de c\u00f3digo abierto", "https://github.com/ftc32477/quick-start-guide"),
            ("Comentarios", "https://github.com/ftc32477/quick-start-guide/issues"),
        ],
    },
    "ko": {
        "heading": "\uc790\ub8cc \ubc0f \uc5c5\ub370\uc774\ud2b8",
        "intro": "\ubcf8 \uac00\uc774\ub4dc\ub294 \uc9c0\uc18d\uc801\uc73c\ub85c \uac1c\uc815\ub429\ub2c8\ub2e4. \ub2e4\uc74c \ucc44\ub110\uc744 \ud1b5\ud574 \ucd5c\uc2e0 \ub0b4\uc6a9\uc744 \ud655\uc778\ud558\uc138\uc694.",
        "items": [
            ("\uc628\ub77c\uc778 \ubc84\uc804", "https://ftc32477.github.io/docs/"),
            ("\ubc84\uc804 \uae30\ub85d", "https://ftc32477.github.io/docs/{lang}/versions.html"),
            ("\uc624\ud508\uc18c\uc2a4 \uc800\uc7a5\uc18c", "https://github.com/ftc32477/quick-start-guide"),
            ("\uc758\uacac \ud53c\ub4dc\ubc31", "https://github.com/ftc32477/quick-start-guide/issues"),
        ],
    },
}


def render_imprint(lang_key):
    """版权页（扉页背面）：完整书名 / 版本号 / 版次 / 发布日期 / 编者 / 出品 / 法律声明，内容置于页面下部。"""
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
    body_font = BODY_FONTS[lang_key]
    font_css = font_faces_css()
    return f"""<!DOCTYPE html>
<html lang="{lang_key}">
<head>
<meta charset="UTF-8">
<style>
{font_css}
@page {{ size: A4; margin: 0; }}
html,body{{margin:0;padding:0}}
.wrap{{
  width:100vw;height:100vh;box-sizing:border-box;padding:1in 1.25in;
  font-family:{body_font};color:#2c2c2c;
  display:flex;flex-direction:column;justify-content:flex-end
}}
table{{width:100%;border-collapse:collapse;font-size:12.5px}}
td{{padding:9px 0;vertical-align:top;border-bottom:1px solid #eee;line-height:1.7}}
td.k{{width:150px;color:#666;padding-right:16px}}
.legal{{margin-top:36px;font-size:10px;color:#666;line-height:1.7}}
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
    """资源与更新页（内页最后一页）：获取渠道链接。"""
    t = dict(RESOURCE_TEXTS["zh-hans"])
    t.update(RESOURCE_TEXTS[lang_key])
    items = "".join(
        f'<tr><td class="k">{k}</td><td><a href="{v.format(lang=lang_key)}">{v.format(lang=lang_key)}</a></td></tr>'
        for k, v in t["items"]
    )
    body_font = BODY_FONTS[lang_key]
    head_font = HEAD_FONTS[lang_key]
    font_css = font_faces_css()
    return f"""<!DOCTYPE html>
<html lang="{lang_key}">
<head>
<meta charset="UTF-8">
<style>
{font_css}
html,body{{margin:0;padding:0}}
.wrap{{font-family:{body_font};color:#2c2c2c;width:100%}}
h1{{font-size:20px;color:#1a1a2e;margin:0 0 6px;font-weight:700;font-family:{head_font}}}
.intro{{font-size:12px;color:#666;margin:0 0 16px;line-height:1.7}}
table{{width:100%;border-collapse:collapse;font-size:12.5px}}
td{{padding:9px 0;vertical-align:top;border-bottom:1px solid #eee;line-height:1.7}}
td.k{{width:150px;color:#666;padding-right:16px}}
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
#  页眉/页脚盖印（reportlab，嵌入字体子集，跨平台一致）
# ============================================================

# 页眉基线距页顶距离（与旧 Chrome 模板 11pt 位置一致）
HEADER_BASELINE_FROM_TOP = 27.0
FOOTER_BASELINE = 0.42 * 72


def _stamp_engine():
    """惰性注册 reportlab 字体（直接嵌入 fonts/subsets/ 的 TTF 子集）。"""
    if getattr(_stamp_engine, "ready", False):
        return
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    registered = set()
    for name, fname in STAMP_FONTS.values():
        if name in registered:
            continue
        path = os.path.join(FONTS_SUBSET_DIR, fname)
        if not os.path.exists(path):
            raise FileNotFoundError(
                f"缺少字体子集 {path}；请先运行 python3 fonts/build_subsets.py"
            )
        pdfmetrics.registerFont(TTFont(name, path))
        registered.add(name)
    _stamp_engine.ready = True


def make_overlay(footer_text, header_left, header_right, page_w, page_h, font_name):
    """生成一页覆盖层：页脚（居中页码）+ 页眉（左站点名 / 右章回名）。"""
    import io
    from reportlab.pdfgen import canvas
    from pypdf import PdfReader

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(page_w, page_h),
                      initialFontName=font_name, initialFontSize=11)
    c.setFont(font_name, 11)
    if header_left or header_right:
        c.setFillColorRGB(0.333, 0.333, 0.333)
        y = page_h - HEADER_BASELINE_FROM_TOP
        if header_left:
            c.drawString(MARGIN_LEFT * 72, y, header_left)
        if header_right:
            c.drawRightString(page_w - MARGIN_RIGHT * 72, y, header_right)
    if footer_text:
        c.setFillColorRGB(0.42, 0.42, 0.42)
        c.drawCentredString(page_w / 2, FOOTER_BASELINE, footer_text)
    c.save()
    buf.seek(0)
    return PdfReader(buf).pages[0]


def stamp_footer(pdf_path, lang_key, header_right=None):
    """为单个 PDF（--page 调试用）的每一页盖印页眉页脚，页码按该 PDF 自身计。"""
    from pypdf import PdfReader, PdfWriter

    _stamp_engine()
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    total = len(reader.pages)
    template = FOOTER_TEXTS[lang_key]
    font_name = STAMP_FONTS[lang_key][0]
    header_left = build_mod.LANGUAGES[lang_key]["site_title"]
    for i, page in enumerate(reader.pages, start=1):
        text = template.format(x=i, y=total)
        overlay = make_overlay(
            text, header_left, header_right,
            float(page.mediabox.width), float(page.mediabox.height), font_name,
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
    body_font = BODY_FONTS[lang_key]
    head_font = HEAD_FONTS[lang_key]
    font_css = font_faces_css()
    return f"""<!DOCTYPE html>
<html lang="{lang_key}">
<head>
<meta charset="UTF-8">
<style>
{font_css}
html,body{{margin:0;padding:0}}
.toc{{
  width:100%;box-sizing:border-box;
  padding:0 0.45in;font-family:{body_font}
}}
.toc h1{{
  font-size:22pt;text-align:center;margin:0 0 30pt;padding-top:28pt;
  font-weight:700;color:#1a1a2e;line-height:1.4;font-family:{head_font}
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
        if not text:
            return
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
    实测 h2 打印字号 Tf = 24.0pt（CSS 24px = 1.5em × 16px），检测范围 23.0–25.0pt。
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


def merge_guide(cover_pdf, title_pdf, imprint_pdf, preface_pdf, toc_pdf, main_pdfs,
                resources_pdf, back_pdf, out_path, lang_key, toc_entries,
                front_blank=False, main_headers=None):
    """
    合并完整指南并盖印页眉页脚（reportlab，嵌入字体子集）。
    按教科书装订方式，封面/封底单独印刷，不印封二封三：
    - 顺序：封面 → 扉页（白底黑字）→ 版权页（扉页背面）→ 前言 → 目录
      → 正文 → 资源页 → 封底
    - 封面/扉页/版权页/资源页/封底不编号、无页眉页脚
    - 页眉：左站点名，右当前章回（前言/目录/各章标题）
    - 前言与目录用罗马数字（仅当前页码，无总页码），前言从 I 连续；
      正文（队员须知起）用阿拉伯数字连续编号
    - toc_entries: [{title, level, dest}]，dest 为全书 0 基目标页；
      按实际渲染的文本行位置注入 PDF 内部超链接
    - 成册规则：front_blank=True 时在目录后插入白页（正文第 1 页位于
      右页/奇数页）；资源页后若页数为偶数，在封底前插入白页，
      保证成册总页数为偶数（内页块页数为偶数）
    """
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import RectangleObject

    _stamp_engine()
    font_name = STAMP_FONTS[lang_key][0]
    arabic_template = FOOTER_TEXTS[lang_key]
    header_left = build_mod.LANGUAGES[lang_key]["site_title"]
    preface_title = build_mod.LANGUAGES[lang_key]["pages"]["preface"]

    writer = PdfWriter()

    def stamp(reader, text_fn, header_right=None):
        for page in reader.pages:
            text = text_fn()
            overlay = make_overlay(
                text, header_left, header_right,
                float(page.mediabox.width), float(page.mediabox.height),
                font_name,
            )
            page.merge_page(overlay, over=True)
            writer.add_page(page)

    # 封面（不编号）
    writer.append(cover_pdf)

    # 扉页（内页第 1 页，白底黑字封面信息，不编号）
    writer.append(title_pdf)

    # 版权页（扉页背面，不编号）
    writer.append(imprint_pdf)

    # 前言：罗马数字，仅当前页码
    preface_reader = PdfReader(preface_pdf)
    roman_counter = 1

    def roman_text():
        nonlocal roman_counter
        label = roman_num(roman_counter)
        roman_counter += 1
        return label

    stamp(preface_reader, roman_text, header_right=preface_title)

    # 目录：罗马数字继续
    toc_reader = PdfReader(toc_pdf)
    toc_start_index = len(writer.pages)
    stamp(toc_reader, roman_text, header_right=TOC_TITLES[lang_key])

    # 补白页尺寸与正文页一致（避免同一文件内 MediaBox 不一致）
    blank_w, blank_h = PAPER_W_IN * 72, PAPER_H_IN * 72
    if main_pdfs:
        _sample = PdfReader(main_pdfs[0]).pages[0].mediabox
        blank_w, blank_h = float(_sample.width), float(_sample.height)

    # 成册：前言+目录为奇数页时，在目录后插入白页（不编页码），
    # 保证正文第 1 页位于右页（物理奇数页）
    if front_blank:
        writer.add_blank_page(width=blank_w, height=blank_h)
        print("  [成册] 前言+目录为奇数页，已在目录后插入白页（正文从右页开始）")

    # 正文：阿拉伯数字连续编号 + 总页数
    total_main = sum(len(PdfReader(p).pages) for p in main_pdfs)
    page_no = 1

    def arabic_text():
        nonlocal page_no
        label = arabic_template.format(x=page_no, y=total_main)
        page_no += 1
        return label

    headers = main_headers or [""] * len(main_pdfs)
    for p, header in zip(main_pdfs, headers):
        stamp(PdfReader(p), arabic_text, header_right=header)

    # 资源与更新页（内页最后一页，不编号、无页眉页脚）
    writer.append(resources_pdf)

    # 印刷成册：资源页后若页数为偶数，则在封底前插入一白页（不编页码），
    # 保证成册总页数为偶数（内页块页数为偶数，便于印刷装订）
    if len(writer.pages) % 2 == 0:
        writer.add_blank_page(width=blank_w, height=blank_h)
        print("  [成册] 资源页后页数为偶数，已在封底前插入白页")

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

    # 书签大纲（章 / 节两级，页码与目录一致；标题解 HTML 实体）
    outline_parent = None
    for entry in toc_entries:
        if entry.get("dest") is None or entry["dest"] >= len(writer.pages):
            continue
        title = html.unescape(entry["title"])
        if entry["level"] == 1:
            outline_parent = writer.add_outline_item(title, entry["dest"])
        elif outline_parent is not None:
            writer.add_outline_item(title, entry["dest"], parent=outline_parent)

    # 文档元数据（阅读器标签与文献管理）
    label = build_mod.LANGUAGES[lang_key]["label"]
    edition = build_mod.latest_edition(lang_key)
    writer.add_metadata({
        "/Title": f"{build_mod.LANGUAGES[lang_key]['site_title']} · {edition}",
        "/Author": "FTC 32477 Origin",
        "/Subject": f"FTC 32477 Origin Quick Start Guide ({label}) · {edition}",
        "/Keywords": f"FTC, FIRST Tech Challenge, 32477 Origin, Quick Start Guide, {label}",
        "/Creator": "FTC 32477 Origin (build_pdf.py)",
    })

    # 统一页面尺寸为精确 A4（210×297mm = 595.276×841.89pt），不缩放内容
    _A4 = RectangleObject([0, 0, 595.276, 841.890])
    for page in writer.pages:
        page.mediabox = _A4
        page.cropbox = _A4

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

        # 构建前校验：该语言 PDF 全部用字须在字体子集覆盖范围内
        for lang in langs:
            if lang in LANGUAGES:
                check_font_coverage(lang)

        pages = [page_filter] if page_filter else PAGE_KEYS

        tmp_dir = tempfile.mkdtemp(prefix="ftc-cover-")

        for lang in langs:
            if lang not in LANGUAGES:
                print(f"  [错误] 未知语言: {lang}")
                continue

            lang_pdf_dir = os.path.join(PDF_DIR, lang)
            os.makedirs(lang_pdf_dir, exist_ok=True)

            rendered = {}  # page_key -> 未盖印页眉页脚的临时 PDF
            for page_key in pages:
                html_path = os.path.join(DIST_DIR, lang, f"{page_key}.html")
                if not os.path.exists(html_path):
                    print(f"  [跳过] {html_path} 不存在（请先运行 python3 build.py）")
                    continue
                chapter = build_mod.LANGUAGES[lang]["pages"][page_key]
                pdf_path = os.path.join(lang_pdf_dir, f"{page_key}.pdf")
                tmp_pdf = os.path.join(tmp_dir, f"{lang}-{page_key}.pdf")
                try:
                    # 渲染正文（注入 PDF 字体；页眉页脚由 reportlab 统一下印）
                    client.navigate("file://" + html_path)
                    inject_pdf_fonts(client, lang, page_key)
                    client.print_to_pdf(tmp_pdf)
                    # 单页 PDF：复制后按自身页数盖印页眉页脚
                    shutil.copyfile(tmp_pdf, pdf_path)
                    stamp_footer(pdf_path, lang, header_right=chapter)
                    rendered[page_key] = tmp_pdf
                    print(f"  [生成] pdf/{lang}/{page_key}.pdf（页眉: {chapter}）")
                except Exception as e:
                    print(f"  [失败] {page_key}: {e}")

            # 完整指南（教科书式装订，封面/封底单独印刷，不印封二封三）：
            # 封面 + 扉页(白底黑字封面信息) + 版权页(扉页背面) + 前言(罗马)
            # + 目录(罗马) + 正文(阿拉伯) + 资源页(内页最后一页) + 封底
            merged_ok = False
            if set(PAGE_KEYS).issubset(rendered) and not page_filter:
                cover_html = os.path.join(tmp_dir, f"cover-{lang}.html")
                title_html = os.path.join(tmp_dir, f"titlepage-{lang}.html")
                back_html = os.path.join(tmp_dir, f"back-{lang}.html")
                imprint_html = os.path.join(tmp_dir, f"imprint-{lang}.html")
                resources_html = os.path.join(tmp_dir, f"resources-{lang}.html")
                toc_html = os.path.join(tmp_dir, f"toc-{lang}.html")
                cover_pdf = os.path.join(tmp_dir, f"cover-{lang}.pdf")
                title_pdf = os.path.join(tmp_dir, f"titlepage-{lang}.pdf")
                back_pdf = os.path.join(tmp_dir, f"back-{lang}.pdf")
                imprint_pdf = os.path.join(tmp_dir, f"imprint-{lang}.pdf")
                resources_pdf = os.path.join(tmp_dir, f"resources-{lang}.pdf")
                toc_pdf = os.path.join(tmp_dir, f"toc-{lang}.pdf")
                with open(cover_html, "w", encoding="utf-8") as f:
                    f.write(render_cover(lang))
                with open(title_html, "w", encoding="utf-8") as f:
                    f.write(render_title_page(lang))
                with open(back_html, "w", encoding="utf-8") as f:
                    f.write(render_back(lang))
                with open(imprint_html, "w", encoding="utf-8") as f:
                    f.write(render_imprint(lang))
                with open(resources_html, "w", encoding="utf-8") as f:
                    f.write(render_resources(lang))
                try:
                    client.navigate("file://" + cover_html)
                    wait_fonts(client)
                    client.print_to_pdf(cover_pdf, margin_top=0, margin_bottom=0,
                                        margin_left=0, margin_right=0)
                    client.navigate("file://" + title_html)
                    wait_fonts(client)
                    client.print_to_pdf(title_pdf, margin_top=0, margin_bottom=0,
                                        margin_left=0, margin_right=0)
                    client.navigate("file://" + back_html)
                    wait_fonts(client)
                    client.print_to_pdf(back_pdf, margin_top=0, margin_bottom=0,
                                        margin_left=0, margin_right=0)
                    client.navigate("file://" + imprint_html)
                    wait_fonts(client)
                    client.print_to_pdf(imprint_pdf, margin_top=0, margin_bottom=0,
                                        margin_left=0, margin_right=0)
                    client.navigate("file://" + resources_html)
                    wait_fonts(client)
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
                    wait_fonts(client)
                    client.print_to_pdf(toc_pdf)

                    # 目标页（全书 0 基）：封面=0，扉页=1，版权页=2，前言从 3 起
                    preface_pages = len(_R(rendered["preface"]).pages)
                    toc_pages = len(_R(toc_pdf).pages)
                    # 成册：前言+目录为奇数页时目录后插白页，正文目标页整体 +1
                    front_blank = (preface_pages + toc_pages) % 2 == 1
                    base = 3 + preface_pages + toc_pages + (1 if front_blank else 0)

                    toc_entries = [
                        {"title": preface_title, "level": 1, "dest": 3}
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
                        cover_pdf, title_pdf, imprint_pdf, rendered["preface"], toc_pdf,
                        [rendered[k] for k in main_keys], resources_pdf, back_pdf,
                        merged_path, lang, toc_entries, front_blank=front_blank,
                        main_headers=[build_mod.LANGUAGES[lang]["pages"][k]
                                      for k in main_keys],
                    )
                    merged_ok = True
                    size_kb = os.path.getsize(merged_path) / 1024
                    print(f"  [合并] FTC-Team-32477-Origin-Quick-Start-Guide-{build_mod.RELEASE_TAG}-{lang}.pdf "
                          f"（封面 + 扉页 + 版权页 + 前言 + 目录（{len(toc_entries)} 行）"
                          f" + {len(main_keys)} 章 + 资源页 + 封底，{size_kb:.0f} KB）")
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
