#!/usr/bin/env python3
"""
FTC 32477 Origin 快速入门指南 — 多语言 Markdown → HTML 构建工具

用法:
    python3 build.py          # 构建所有语言版本
    python3 build.py --watch  # 监听文件变化并自动构建

目录结构:
    src/{zh-cn,zh-tw,en}/   — 各语言 Markdown 源文件（在此编辑内容）
    images/                 — 图片资源（自动复制到 dist/images/）
    dist/                   — 生成的 HTML 网站（含各语言子目录）
"""

import os
import re
import sys
import time
import shutil
import hashlib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
IMAGES_DIR = os.path.join(BASE_DIR, "images")
DIST_DIR = os.path.join(BASE_DIR, "dist")

# 页面清单（page_key 为所有语言共用）
PAGE_KEYS = [
    "index",
    "member",
    "modeling",
    "build",
    "programming",
    "outreach",
    "afterword",
]

# 各语言配置
LANGUAGES = {
    "zh-cn": {
        "label": "简体中文",
        "brand": "快速入门指南",
        "footer": "2026年8月第1版 &middot; 编写小组",
        "site_title": "FTC 32477 Origin 快速入门指南",
        "pages": {
            "index":       "前言",
            "member":      "队员须知",
            "modeling":    "建模设计",
            "build":       "结构建造",
            "programming": "程序设计",
            "outreach":    "外部联络",
            "afterword":   "后记",
        },
    },
    "zh-tw": {
        "label": "繁體中文",
        "brand": "快速入門指南",
        "footer": "2026年8月第1版 &middot; 編寫小組",
        "site_title": "FTC 32477 Origin 快速入門指南",
        "pages": {
            "index":       "前言",
            "member":      "隊員須知",
            "modeling":    "建模設計",
            "build":       "結構建造",
            "programming": "程式設計",
            "outreach":    "外部聯絡",
            "afterword":   "後記",
        },
    },
    "en-us": {
        "label": "English (US)",
        "brand": "Quick Start Guide",
        "footer": "Aug 2026, 1st Ed. &middot; Editorial Team",
        "site_title": "FTC 32477 Origin Quick Start Guide",
        "pages": {
            "index":       "Preface",
            "member":      "Team Essentials",
            "modeling":    "Modeling &amp; Design",
            "build":       "Hardware &amp; Build",
            "programming": "Programming",
            "outreach":    "Outreach &amp; PR",
            "afterword":   "Afterword",
        },
    },
    "fr": {
        "label": "Français",
        "brand": "Guide de démarrage rapide",
        "footer": "Août 2026, 1re éd. &middot; Équipe éditoriale",
        "site_title": "Guide de démarrage rapide FTC 32477 Origin",
        "pages": {
            "index":       "Préface",
            "member":      "Essentiels de l'équipe",
            "modeling":    "Modélisation &amp; Conception",
            "build":       "Matériel &amp; Construction",
            "programming": "Programmation",
            "outreach":    "Sensibilisation &amp; Relations publiques",
            "afterword":   "Postface",
        },
    },
}

DEFAULT_LANG = "zh-cn"


# ============================================================
#  MARKDOWN → HTML 转换器
# ============================================================

def parse_markdown(text):
    """
    将 Markdown 文本转换为 HTML。

    返回 (html, headings)，其中 headings 为 h2/h3 标题列表，
    每项为 {"level": int, "id": str, "text": str}，供侧边栏二级目录使用。
    """
    lines = text.split("\n")
    out = []
    headings = []
    used_ids = {}
    i = 0

    def flush_paragraph(buf):
        if buf:
            content = "\n".join(buf)
            out.append(f"<p>{inline_parse(content)}</p>")
            buf.clear()

    para_buf = []

    while i < len(lines):
        line = lines[i]

        # 代码块
        if line.strip().startswith("```"):
            flush_paragraph(para_buf)
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1
            code_html = escape_html("\n".join(code_lines))
            out.append(f"<pre><code>{code_html}</code></pre>")
            continue

        # 图片 ![](url)（连续多张自动合并为横向排布）
        img_match = re.match(r"^!\[(.*?)\]\((.*?)\)\s*$", line.strip())
        if img_match:
            flush_paragraph(para_buf)
            imgs = []
            while i < len(lines):
                m = re.match(r"^!\[(.*?)\]\((.*?)\)\s*$", lines[i].strip())
                if not m:
                    break
                alt = m.group(1)
                src = m.group(2)
                caption = f'<figcaption>{escape_html(alt)}</figcaption>' if alt else ""
                imgs.append(
                    f'<figure class="img-fig">'
                    f'<img src="{src}" alt="{escape_html(alt)}" loading="lazy">{caption}</figure>'
                )
                i += 1
            if len(imgs) > 1:
                out.append('<div class="img-row">' + "".join(imgs) + "</div>")
            else:
                out.append('<div class="img-row img-row-single">' + "".join(imgs) + "</div>")
            continue

        # 表格
        if "|" in line and line.strip().startswith("|"):
            flush_paragraph(para_buf)
            table_lines = []
            while i < len(lines) and "|" in lines[i] and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1

            if len(table_lines) >= 2:
                out.append(render_table(table_lines))
            else:
                for tl in table_lines:
                    out.append(f"<p>{inline_parse(tl.strip())}</p>")
            continue

        # 水平线
        if re.match(r"^[-*_]{3,}\s*$", line.strip()):
            flush_paragraph(para_buf)
            out.append("<hr>")
            i += 1
            continue

        # 标题
        heading_match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading_match:
            flush_paragraph(para_buf)
            level = len(heading_match.group(1))
            content = heading_match.group(2).strip()
            content = re.sub(r"\s+#+\s*$", "", content)
            if level in (2, 3):
                plain = plain_text(content)
                hid = slugify(plain)
                if hid in used_ids:
                    used_ids[hid] += 1
                    hid = f"{hid}-{used_ids[hid]}"
                else:
                    used_ids[hid] = 0
                headings.append({"level": level, "id": hid, "text": plain})
                out.append(f'<h{level} id="{hid}">{inline_parse(content)}</h{level}>')
            else:
                out.append(f"<h{level}>{inline_parse(content)}</h{level}>")
            i += 1
            continue

        # 无序列表
        ul_match = re.match(r"^(\s*)[-*+]\s+(.+)$", line)
        if ul_match:
            flush_paragraph(para_buf)
            list_html, i = parse_list(lines, i, len(ul_match.group(1)), ordered=False)
            out.append(list_html)
            continue

        # 有序列表
        ol_match = re.match(r"^(\s*)\d+\.\s+(.+)$", line)
        if ol_match:
            flush_paragraph(para_buf)
            list_html, i = parse_list(lines, i, len(ol_match.group(1)), ordered=True)
            out.append(list_html)
            continue

        # 引用（支持第一行 [!info] / [!warning] / [!danger] 类型标记）
        blockquote_match = re.match(r"^>\s?(.*)$", line)
        if blockquote_match:
            flush_paragraph(para_buf)
            bq_lines = []
            bq_class = None
            while i < len(lines):
                m = re.match(r"^>\s?(.*)$", lines[i])
                if not m:
                    break
                if bq_class is None:
                    tm = re.match(r"^\[!(info|warning|danger)\]\s?(.*)$", m.group(1))
                    if tm:
                        bq_class = tm.group(1)
                        if tm.group(2):
                            bq_lines.append(tm.group(2))
                    else:
                        bq_lines.append(m.group(1))
                else:
                    bq_lines.append(m.group(1))
                i += 1
            bq_content = inline_parse(" ".join(bq_lines))
            cls = f' class="bq-{bq_class}"' if bq_class else ""
            out.append(f"<blockquote{cls}>{bq_content}</blockquote>")
            continue

        # 空行 → 段落边界
        if line.strip() == "":
            flush_paragraph(para_buf)
            i += 1
            continue

        # 普通文本行
        para_buf.append(line)
        i += 1

    flush_paragraph(para_buf)
    return "\n".join(out), headings


def plain_text(md_text):
    """去除行内 Markdown 标记，返回纯文本（用于目录显示）。"""
    text = re.sub(r"!\[(.*?)\]\((.*?)\)", r"\1", md_text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[*_`]", "", text)
    return text.strip()


def slugify(text):
    """生成标题锚点 ID：保留中英文数字，其余字符去除。"""
    slug = re.sub(r"[^\w\u4e00-\u9fff-]", "", text, flags=re.UNICODE)
    return slug or "section"


def parse_list(lines, i, indent, ordered):
    """
    递归解析列表（支持嵌套）。

    lines[i] 是列表的第一项，其缩进为 indent。
    返回 (html, next_index)。
    """
    tag = "ol" if ordered else "ul"
    items = []

    while i < len(lines):
        line = lines[i]
        m = re.match(r"^(\s*)(\d+\.|[+\-*])\s+(.+)$", line)
        if not m:
            break
        cur_indent = len(m.group(1))
        if cur_indent < indent or cur_indent > indent:
            break

        content = inline_parse(m.group(3).strip())
        items.append({"content": content, "sub": ""})
        i += 1

        # 检查紧邻的嵌套子列表
        while i < len(lines):
            sub = re.match(r"^(\s*)(\d+\.|[+\-*])\s+(.+)$", lines[i])
            if sub and len(sub.group(1)) > cur_indent:
                sub_html, i = parse_list(
                    lines, i, len(sub.group(1)),
                    ordered=sub.group(2).rstrip(".").isdigit()
                )
                items[-1]["sub"] += sub_html
                continue
            break

    html = f"<{tag}>"
    for item in items:
        html += f"<li>{item['content']}{item['sub']}</li>"
    html += f"</{tag}>"
    return html, i


def inline_parse(text):
    """解析行内元素。"""
    # 图片（行内）
    text = re.sub(r"!\[(.*?)\]\((.*?)\)", r'<img src="\2" alt="\1" loading="lazy">', text)
    # 链接
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank">\1</a>', text)
    # 粗斜体
    text = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", text)
    # 粗体
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    # 斜体
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    # 行内代码
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def escape_html(text):
    """转义 HTML 特殊字符。"""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render_table(lines):
    """渲染 Markdown 表格。"""
    def split_cells(l):
        return [c.strip() for c in l.strip().strip("|").split("|")]

    header = split_cells(lines[0])
    alignments = []
    if len(lines) >= 2 and re.match(r"^[\|\s\-:]+$", lines[1]):
        align_row = split_cells(lines[1])
        for cell in align_row:
            if cell.startswith(":") and cell.endswith(":"):
                alignments.append("center")
            elif cell.endswith(":"):
                alignments.append("right")
            else:
                alignments.append("left")
        body_start = 2
    else:
        body_start = 1
        alignments = ["left"] * len(header)

    thead = "<thead><tr>" + "".join(
        f'<th style="text-align:{alignments[j] if j < len(alignments) else "left"}">{inline_parse(h)}</th>'
        for j, h in enumerate(header)
    ) + "</tr></thead>"

    tbody_rows = []
    for row_line in lines[body_start:]:
        cells = split_cells(row_line)
        tbody_rows.append(
            "<tr>" + "".join(
                f'<td style="text-align:{alignments[j] if j < len(alignments) else "left"}">{inline_parse(c)}</td>'
                for j, c in enumerate(cells)
            ) + "</tr>"
        )
    tbody = "<tbody>" + "".join(tbody_rows) + "</tbody>"

    return f'<div class="table-wrap"><table>{thead}{tbody}</table></div>'


# ============================================================
#  HTML 公共样式
# ============================================================

CSS = r"""
:root {
  --red: #d32f2f;
  --dark: #1a1a2e;
  --slate: #16213e;
  --card: #ffffff;
  --text: #2c2c2c;
  --muted: #666;
  --border: #e0e0e0;
  --radius: 10px;
  --sidebar-w: 260px;
  --topbar-h: 52px;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei","Noto Sans SC",sans-serif;
  color:var(--text);background:#f8f9fa;line-height:1.8;min-height:100vh
}

/* ====== TOP BAR (mobile) ====== */
.topbar{
  display:none;position:fixed;top:0;left:0;right:0;height:var(--topbar-h);
  background:var(--dark);color:#fff;z-index:200;align-items:center;
  padding:0 12px;gap:8px
}
.topbar .brand{
  font-weight:700;font-size:14px;flex:1;min-width:0;
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap
}
.topbar .brand a{
  color:#fff;text-decoration:none;cursor:pointer
}
.topbar .brand a:hover{opacity:.85}
.lang-select{
  background:rgba(255,255,255,.1);color:#fff;border:1px solid rgba(255,255,255,.25);
  border-radius:6px;font-size:13px;padding:6px 26px 6px 10px;max-width:150px;
  appearance:none;-webkit-appearance:none;cursor:pointer;
  background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6' viewBox='0 0 10 6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%23aaa'/%3E%3C/svg%3E");
  background-repeat:no-repeat;background-position:right 8px center
}
.lang-select option{color:#2c2c2c;background:#fff}
.topbar .menu-btn{
  background:none;border:none;color:#fff;font-size:24px;cursor:pointer;
  width:40px;height:40px;flex-shrink:0;display:flex;align-items:center;
  justify-content:center;border-radius:6px;line-height:1
}
.topbar .menu-btn:hover{background:rgba(255,255,255,.1)}

/* ====== SIDEBAR ====== */
nav.sidebar{
  position:fixed;top:0;left:0;bottom:0;width:var(--sidebar-w);
  background:var(--dark);color:#ccc;overflow-y:auto;z-index:100;
  display:flex;flex-direction:column;transition:transform .28s ease;
}
nav.sidebar::-webkit-scrollbar{width:4px}
nav.sidebar::-webkit-scrollbar-thumb{background:#444;border-radius:2px}
.sidebar-header{padding:24px 20px 14px;border-bottom:1px solid rgba(255,255,255,.08);text-align:center}
.sidebar-header .home-link{
  display:block;text-decoration:none;border-radius:8px;
  padding:4px 0;transition:background .18s
}
.sidebar-header .home-link:hover{background:rgba(255,255,255,.06)}
.sidebar-header .home-link:hover .sub{color:#fff}
.sidebar-header .logo{font-size:22px;font-weight:700;color:#fff;line-height:1.3}
.sidebar-header .sub{font-size:12px;color:#f44336;margin-top:4px;letter-spacing:1px}
/* 语言切换：侧边栏下拉选项栏（节省空间给目录） */
.lang-select-sidebar{
  margin:12px 14px 0;width:calc(100% - 28px);box-sizing:border-box;
  background:rgba(255,255,255,.1);color:#fff;
  border:1px solid rgba(255,255,255,.25);border-radius:8px;
  font-size:13px;padding:7px 26px 7px 10px;
  appearance:none;-webkit-appearance:none;cursor:pointer;
  background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6' viewBox='0 0 10 6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%23aaa'/%3E%3C/svg%3E");
  background-repeat:no-repeat;background-position:right 8px center
}
.lang-select-sidebar option{color:#2c2c2c;background:#fff}
.sidebar-nav{flex:1;padding:12px 0}
.sidebar-nav a{
  display:block;padding:10px 22px;color:#aaa;text-decoration:none;
  font-size:14px;border-left:3px solid transparent;transition:all .18s
}
.sidebar-nav a:hover{color:#fff;background:rgba(255,255,255,.04)}
.sidebar-nav a.active{color:#fff;background:rgba(244,67,54,.15);border-left-color:#f44336}
/* 二级目录：仅当前页面显示 */
.sidebar-nav a.sub-link{
  padding:5px 22px 5px 34px;font-size:12.5px;color:#8a8a8a;border-left-color:transparent
}
.sidebar-nav a.sub-link:hover{color:#fff}
.sidebar-nav a.sub-link.sub-3{padding-left:46px;font-size:12px;color:#777}
/* 侧边栏队徽 */
.side-logo{
  display:block;width:64px;height:64px;margin:0 auto 10px;
  border-radius:14px;object-fit:cover
}
/* 顶栏队徽（移动端） */
.topbar-logo{width:22px;height:22px;border-radius:5px;flex-shrink:0}
.sidebar-footer{padding:16px 20px;font-size:11px;color:#555;border-top:1px solid rgba(255,255,255,.08);text-align:center}

/* ====== OVERLAY (mobile) ====== */
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.4);z-index:99}

/* ====== MAIN CONTENT ====== */
/*
 * 响应式宽度策略：
 *   宽屏：内容固定 900px 宽（含 padding），居中于侧边栏右侧
 *   中屏：随宽度缩小，左右留白逐渐收窄直至消失
 *   窄屏（<768px）：侧边栏折叠，内容全宽
 *
 * 兼容性说明：部分 Chrome 版本对嵌套在自定义属性中的
 * min()/max()/clamp()（含 vw 单位）存在布局计算 bug（宽度会算成 0，
 * 正文空白而侧边栏正常）。因此此处只用普通 calc + max-width 封顶，
 * 并为 min()/max()/clamp() 提供级联回退声明。
 */
main{
  box-sizing:content-box;
  --pad: 40px;                                        /* 回退：clamp 不支持时 */
  --pad: clamp(12px, 4vw, 48px);
  padding: 40px var(--pad);
  /* 宽度：随视口收缩，上限 900px（含 padding，即内容宽 900-2*pad） */
  width: calc(100vw - var(--sidebar-w) - 2 * var(--pad));
  max-width: calc(900px - 2 * var(--pad));
  /* 左外边距：回退为紧贴侧边栏，支持 max() 时在宽屏居中 */
  margin-left: var(--sidebar-w);
  margin-left: calc(var(--sidebar-w) + max(0px, (100vw - var(--sidebar-w) - 900px) / 2));
  margin-right: auto;
}

/* Hero */
.hero{
  background:linear-gradient(135deg,var(--dark) 0%,var(--slate) 100%);color:#fff;
  border-radius:var(--radius);padding:44px 40px;margin-bottom:36px;
  position:relative;overflow:hidden
}
.hero::after{
  content:'';position:absolute;right:-40px;bottom:-40px;
  width:200px;height:200px;background:var(--red);opacity:.18;border-radius:50%
}
.hero h1{font-size:28px;font-weight:700;position:relative;z-index:1}
.hero .subtitle{font-size:14px;margin-top:10px;opacity:.8;position:relative;z-index:1}
.hero .badge{
  display:inline-block;background:var(--red);padding:4px 14px;
  border-radius:20px;font-size:12px;font-weight:600;margin-bottom:12px;
  position:relative;z-index:1
}

/* Sections */
section{margin-bottom:40px}
section h2{font-size:22px;font-weight:700;padding-bottom:10px;margin-bottom:20px;border-bottom:2px solid var(--red);color:var(--dark)}
section h3{font-size:17px;font-weight:600;margin:28px 0 10px;color:var(--slate)}
section h4,.card h4{font-size:15px;font-weight:600;margin:18px 0 8px}
.card{background:var(--card);border-radius:var(--radius);padding:24px 28px;box-shadow:0 1px 4px rgba(0,0,0,.04);margin-bottom:16px}
p{margin-bottom:10px}
a{color:#1565c0;text-decoration:none;overflow-wrap:anywhere}
a:hover{text-decoration:underline}
ul,ol{padding-left:22px;margin-bottom:12px}
li{margin-bottom:4px}
code{background:#f0f0f0;padding:2px 6px;border-radius:4px;font-size:13px;font-family:"SF Mono","Fira Code",monospace}
pre{background:#1a1a2e;color:#e0e0e0;padding:16px 20px;border-radius:var(--radius);overflow-x:auto;margin-bottom:14px;font-size:13px;line-height:1.6}
pre code{background:none;padding:0;color:inherit}
blockquote{
  border-left:4px solid var(--red);background:#fef5f5;padding:12px 18px;
  margin:14px 0;border-radius:0 var(--radius) var(--radius) 0;font-size:14px;color:#8b0000
}
/* 类型化引用块：[!info] 蓝 / [!warning] 黄 / [!danger] 红（仅颜色区分，无标签） */
blockquote.bq-info{border-left-color:#1565c0;background:#eaf3fb;color:#0d3c66}
blockquote.bq-warning{border-left-color:#f9a825;background:#fff8e1;color:#6d4c00}
blockquote.bq-danger{border-left-color:#d32f2f;background:#fef5f5;color:#8b0000}
hr{border:none;border-top:1px solid var(--border);margin:24px 0}
img{max-width:100%;border-radius:var(--radius);margin:12px 0}
/* 锚点跳转留白（避免被固定顶栏遮挡） */
h2,h3{scroll-margin-top:16px}

/* 图片排布：多图横向，窄屏自动纵向 */
.img-row{
  display:flex;flex-wrap:wrap;gap:14px;margin:14px 0
}
.img-row .img-fig{
  flex:1 1 40%;min-width:0;margin:0
}
.img-row .img-fig img{
  width:100%;margin:0;border-radius:var(--radius)
}
.img-row figcaption{
  text-align:center;font-size:12px;color:var(--muted);margin-top:6px
}
.img-row-single .img-fig{flex-basis:100%}
@media(max-width:600px){
  .img-row{flex-direction:column;gap:12px}
  h2,h3{scroll-margin-top:64px}
}

/* Table */
.table-wrap{overflow-x:auto;margin-bottom:14px}
table{width:100%;border-collapse:collapse;font-size:14px}
th,td{border:1px solid var(--border);padding:10px 14px;text-align:left}
th{background:var(--dark);color:#fff;font-weight:600}
tr:nth-child(even){background:#fafafa}

/* ====== RESPONSIVE ====== */

/* Narrow: collapse sidebar */
@media(max-width:768px){
  .topbar{display:flex}
  nav.sidebar{
    transform:translateX(-100%);
    top:var(--topbar-h);z-index:101;
    width:280px;                        /* 回退：min() 不支持时 */
    width:min(280px,84vw)
  }
  nav.sidebar.open{transform:translateX(0)}
  .overlay.show{display:block}
  main{
    margin-left:0;margin-top:var(--topbar-h);
    width: calc(100vw - 2 * var(--pad));
    max-width: none;
  }
  .hero{padding:28px 20px}
  .hero h1{font-size:22px}
  .card{padding:16px 18px}
  section h2{font-size:19px}
  section h3{font-size:16px}
  .table-wrap{margin-left:-18px;margin-right:-18px;width:calc(100% + 36px)}
}

/* Very narrow screens */
@media(max-width:420px){
  .topbar .brand{font-size:13px}
  .lang-select{max-width:132px;font-size:12px;padding:5px 22px 5px 8px}
  main{--pad: 12px}
  .card{padding:14px 14px}
  .hero{padding:22px 16px}
  .hero h1{font-size:20px}
}

/* ====== PRINT (PDF 导出) ====== */
/*
 * 注意：Chrome 打印视口宽度可能低于 768px，导致移动端媒体查询规则
 * 泄漏到打印渲染。因此必须在打印样式中显式覆盖所有相关属性。
 */
@media print{
  html,body{display:block !important;width:100% !important;max-width:100% !important;overflow:visible !important}
  nav.sidebar,.topbar,.overlay{display:none !important}
  body{background:#fff}
  main{
    display:block !important;box-sizing:border-box !important;
    margin:0 !important;padding:0 !important;
    width:100% !important;max-width:100% !important;
  }
  .card{box-shadow:none;border:1px solid var(--border);padding:24px 28px}
  .hero{background:#fff;color:var(--text);border:1px solid var(--border);padding:32px 28px}
  .hero h1{color:var(--dark);font-size:28px}
  section h2{font-size:22px}
  section h3{font-size:17px}
  .hero .badge{background:var(--red);color:#fff}
  a{color:inherit;overflow-wrap:anywhere !important}
  /* 表格打印适配：覆盖移动端负边距泄漏，强制约束在页面宽度内 */
  .table-wrap{
    overflow:visible !important;
    margin:0 !important;
    width:100% !important;
    max-width:100% !important;
  }
  table{
    width:100% !important;max-width:100% !important;
    table-layout:fixed;font-size:12px
  }
  th,td{padding:6px 8px;word-break:break-all;overflow-wrap:break-word}
  tr{page-break-inside:avoid}
  .img-row{flex-wrap:nowrap}
  .img-fig{page-break-inside:avoid}
  .img-row .img-fig{flex:1 1 0}
  /* 中文版段落首行缩进 2 字符（英文版按英文规范不缩进） */
  html[lang="zh-cn"] main p,html[lang="zh-tw"] main p{text-indent:2em}
  /* 标题间距：一级标题前空约两行，二级标题前空约一行 */
  h1{margin:3.2em 0 1em}
  h2{margin:2em 0 .8em}
  h3{margin:1.2em 0 .5em}
}
"""


# ============================================================
#  页面生成
# ============================================================

def render_page(page_key, html_body, lang_key, headings=None):
    """将 HTML 正文包装进完整页面模板。"""
    lang = LANGUAGES[lang_key]
    headings = headings or []

    # 侧边栏导航（当前语言的页面标题 + 当前页的二级目录）
    nav_items = []
    for key in PAGE_KEYS:
        cls = ' class="active"' if key == page_key else ""
        title = lang["pages"][key]
        nav_items.append(f'<a href="{key}.html"{cls}>{title}</a>')
        if key == page_key:
            for h in headings:
                sub_cls = "sub-link" + (" sub-3" if h["level"] == 3 else "")
                nav_items.append(
                    f'<a class="{sub_cls}" href="#{h["id"]}">{escape_html(h["text"])}</a>'
                )
    nav_html = "\n".join(nav_items)

    # 语言切换：侧边栏下拉选项栏（节省空间给目录）
    sidebar_options = []
    for lk, lc in LANGUAGES.items():
        sel = " selected" if lk == lang_key else ""
        sidebar_options.append(
            f'<option value="../{lk}/{page_key}.html"{sel}>{lc["label"]}</option>'
        )
    sidebar_select_html = "".join(sidebar_options)

    # 语言切换：移动端顶栏下拉选项栏
    select_options = []
    for lk, lc in LANGUAGES.items():
        sel = " selected" if lk == lang_key else ""
        select_options.append(
            f'<option value="../{lk}/{page_key}.html"{sel}>{lc["label"]}</option>'
        )
    select_html = "".join(select_options)

    page_title = lang["pages"][page_key]
    site_title = lang["site_title"]

    return f"""<!DOCTYPE html>
<html lang="{lang_key}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}\uff5c{site_title}</title>
<link rel="icon" href="../images/basic/icon_team_logo.ico" type="image/x-icon">
<link rel="shortcut icon" href="../images/basic/icon_team_logo.ico" type="image/x-icon">
<style>{CSS}</style>
</head>
<body>

<div class="topbar">
  <img class="topbar-logo" src="../images/basic/team_logo.png" alt="32477 Origin">
  <span class="brand"><a href="../index.html" title="\u8fd4\u56de\u4e3b\u9875">{site_title}</a></span>
  <select class="lang-select" id="langSelect" aria-label="Language">
{select_html}
  </select>
  <button class="menu-btn" id="menuBtn" aria-label="Menu">\u2630</button>
</div>
<div class="overlay" id="overlay"></div>

<nav class="sidebar" id="sidebar">
  <div class="sidebar-header">
    <a class="home-link" href="../index.html" title="\u8fd4\u56de\u4e3b\u9875">
      <img class="side-logo" src="../images/basic/team_logo.png" alt="32477 Origin Team Logo">
      <div class="logo">FTC 32477<br>Origin</div>
      <div class="sub">{lang["brand"]}</div>
    </a>
    <select class="lang-select-sidebar" id="langSelectSide" aria-label="Language">
{sidebar_select_html}
    </select>
  </div>
  <div class="sidebar-nav">
{nav_html}
  </div>
  <div class="sidebar-footer">{lang["footer"]}</div>
</nav>

<main>
{html_body}
</main>

<script>
(function(){{
  var sb=document.getElementById("sidebar");
  var ol=document.getElementById("overlay");
  var btn=document.getElementById("menuBtn");
  function open(){{sb.classList.add("open");ol.classList.add("show")}}
  function close(){{sb.classList.remove("open");ol.classList.remove("show")}}
  btn.addEventListener("click",function(){{sb.classList.contains("open")?close():open()}});
  ol.addEventListener("click",close);
  var ls=document.getElementById("langSelect");
  if(ls){{ls.addEventListener("change",function(){{window.location.href=ls.value}})}};
  var lss=document.getElementById("langSelectSide");
  if(lss){{lss.addEventListener("change",function(){{window.location.href=lss.value}})}};
}})();
</script>
</body>
</html>"""


# ============================================================
#  主页（语言选择落地页）
# ============================================================

HOMEPAGE_CSS = r"""
:root {
  --red: #d32f2f;
  --dark: #1a1a2e;
  --slate: #16213e;
  --card: #ffffff;
  --text: #2c2c2c;
  --muted: #666;
  --border: #e0e0e0;
  --radius: 12px;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei","Noto Sans SC",sans-serif;
  color:var(--text);background:#f8f9fa;line-height:1.8;min-height:100vh
}

/* Hero */
.hero{
  background:linear-gradient(135deg,var(--dark) 0%,var(--slate) 100%);
  color:#fff;text-align:center;padding:72px 32px 64px;position:relative;overflow:hidden
}
.hero::before{
  content:'';position:absolute;left:-80px;top:-80px;width:260px;height:260px;
  background:var(--red);opacity:.12;border-radius:50%
}
.hero::after{
  content:'';position:absolute;right:-60px;bottom:-60px;width:220px;height:220px;
  background:var(--red);opacity:.15;border-radius:50%
}
.hero .badge{
  display:inline-block;background:var(--red);padding:5px 16px;border-radius:20px;
  font-size:12px;font-weight:600;letter-spacing:1px;margin-bottom:16px;
  position:relative;z-index:1
}
.hero .hero-logo{
  width:96px;height:96px;border-radius:20px;margin:0 auto 18px;
  display:block;position:relative;z-index:1;box-shadow:0 4px 16px rgba(0,0,0,.25)
}
.hero h1{font-size:34px;font-weight:700;position:relative;z-index:1;line-height:1.35}
.hero .subtitle{font-size:15px;margin-top:12px;opacity:.85;position:relative;z-index:1}

/* Container */
.container{max-width:860px;margin:0 auto;padding:40px 20px 64px}
section{margin-bottom:44px}
section>h2{
  font-size:21px;font-weight:700;margin-bottom:18px;color:var(--dark);
  padding-bottom:10px;border-bottom:2px solid var(--red)
}
/* 中英文内容同字号同深度，以示平等 */
section>h2 .en{font-size:inherit;color:inherit;font-weight:inherit;margin-left:10px}

/* About：简洁纵向列表 */
.about-simple{background:var(--card);border-radius:var(--radius);padding:6px 24px;box-shadow:0 1px 4px rgba(0,0,0,.04)}
.about-line{
  display:flex;align-items:baseline;gap:14px;padding:14px 0;
  border-bottom:1px solid var(--border);font-size:15px;margin:0
}
.about-line:last-child{border-bottom:none}
.about-line .tag-label{
  font-size:12px;color:var(--muted);min-width:70px;flex-shrink:0;
  background:#f0f0f0;padding:3px 10px;border-radius:12px;text-align:center
}
.about-line .text{font-weight:500}
.about-line .text .en{color:inherit;font-weight:inherit;font-size:inherit;margin-left:8px}

/* Language cards */
.lang-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:18px}
.lang-card{
  background:var(--card);border-radius:var(--radius);padding:28px 24px;
  box-shadow:0 2px 8px rgba(0,0,0,.05);display:flex;flex-direction:column;
  transition:transform .18s,box-shadow .18s;border-top:3px solid transparent
}
.lang-card:hover{transform:translateY(-3px);box-shadow:0 8px 20px rgba(0,0,0,.09)}
.lang-card.zh-cn{border-top-color:var(--red)}
.lang-card.zh-tw{border-top-color:#e65100}
.lang-card.en-us{border-top-color:#1565c0}
.lang-card.fr{border-top-color:#0055a4}
.lang-card h3{font-size:18px;font-weight:700;margin-bottom:4px}
.lang-card .lang-name{font-size:13px;color:var(--muted);margin-bottom:12px}
.lang-card .desc{font-size:13px;color:var(--text);flex:1;margin-bottom:18px}
.lang-card .btn-row{display:flex;flex-direction:column;gap:8px}
.btn{
  display:block;text-align:center;padding:10px 0;border-radius:8px;
  font-size:14px;font-weight:600;text-decoration:none;transition:all .18s
}
.btn:hover{text-decoration:none}
.btn.primary{background:var(--dark);color:#fff}
.btn.primary:hover{background:var(--slate)}
.btn.secondary{background:#f0f0f0;color:var(--text)}
.btn.secondary:hover{background:#e4e4e4}
.btn.disabled{background:#f5f5f5;color:#aaa;cursor:not-allowed;pointer-events:none}
.lang-card .pdf-note{font-size:11px;color:#c62828;margin-top:8px;text-align:center}

/* Chapters */
.chapter-list{list-style:none}
.chapter-list li{
  display:flex;align-items:center;gap:14px;padding:11px 16px;
  background:var(--card);border-radius:8px;margin-bottom:8px;
  box-shadow:0 1px 4px rgba(0,0,0,.04);font-size:14px
}
.chapter-list .num{
  width:28px;height:28px;border-radius:50%;background:var(--red);color:#fff;
  display:flex;align-items:center;justify-content:center;font-size:12px;
  font-weight:700;flex-shrink:0
}
.chapter-list .name{font-weight:600;min-width:120px}
.chapter-list .names{font-size:13px;color:var(--muted)}

/* Footer */
footer{
  text-align:center;padding:32px 20px;color:var(--muted);font-size:12px;
  border-top:1px solid var(--border)
}
/* 底部法律声明：中英文同字号同深度，以示平等 */
footer .legal{margin-top:20px;font-size:11px;color:#9a9a9a;line-height:1.8;padding:0 12px}
footer .legal p{margin:0 0 8px}
footer .legal p:last-child{margin-bottom:0}

@media(max-width:600px){
  .hero{padding:48px 20px 44px}
  .hero h1{font-size:24px}
  .hero .subtitle{font-size:14px}
  .container{padding:28px 16px 48px}
  section>h2{font-size:19px}
  .lang-grid{grid-template-columns:1fr}
  .chapter-list .names{display:none}
  .chapter-list li{gap:10px;padding:10px 12px}
  .chapter-list .name{min-width:0;font-size:14px}
  .about-simple{padding:4px 16px}
  .about-line{flex-direction:column;gap:6px;padding:12px 0;font-size:14px}
  .about-line .tag-label{align-self:flex-start}
}

/* Very narrow screens */
@media(max-width:380px){
  .hero{padding:40px 14px 36px}
  .hero h1{font-size:21px}
  .hero .badge{font-size:11px}
  .container{padding:22px 12px 40px}
  .lang-card{padding:20px 16px}
  .btn{font-size:13px;padding:9px 0}
}
"""


def render_homepage():
    """生成主页（语言选择落地页）。"""
    # 三种语言的卡片
    lang_cards = []

    def pdf_link(lang_key, filename):
        pdf_path = os.path.join(DIST_DIR, "pdf", filename)
        if os.path.exists(pdf_path):
            return (
                f'<a class="btn secondary" href="pdf/{filename}" target="_blank" rel="noopener">'
                f'\u2193 \u4e0b\u8f7d PDF</a>'
            )
        return (
            f'<a class="btn disabled" title="\u8bf7\u5148\u8fd0\u884c python3 build_pdf.py">'
            f'\u2193 PDF \u5c1a\u672a\u751f\u6210</a>'
            f'<div class="pdf-note">\u8fd0\u884c python3 build_pdf.py \u751f\u6210 PDF</div>'
        )

    lang_cards.append(f"""
<div class="lang-card zh-cn">
  <h3>\u7b80\u4f53\u4e2d\u6587</h3>
  <div class="lang-name">Simplified Chinese</div>
  <div class="desc">\u9762\u5411\u4e2d\u56fd\u5927\u9646\u961f\u5458\u7684\u7b80\u4f53\u4e2d\u6587\u5728\u7ebf\u7248\u672c\uff0c\u5305\u542b\u5168\u90e8 7 \u4e2a\u7ae0\u8282\u3002<br>Online edition in Simplified Chinese, covering all 7 chapters.</div>
  <div class="btn-row">
    <a class="btn primary" href="zh-cn/index.html">\u5728\u7ebf\u6d4f\u89c8 \u2192</a>
    {pdf_link("zh-cn", "FTC-Team-32477-Origin-Quick-Start-Guide-2026-08-01-zh-cn.pdf")}
  </div>
</div>""")

    lang_cards.append(f"""
<div class="lang-card zh-tw">
  <h3>\u7e41\u4f53\u4e2d\u6587</h3>
  <div class="lang-name">Traditional Chinese</div>
  <div class="desc">\u9762\u5411\u4f7f\u7528\u7e41\u9ad4\u4e2d\u6587\u7684\u968a\u54e1\u7684\u5728\u7dda\u7248\u672c\uff0c\u542b\u5168\u90e8 7 \u500b\u7ae0\u7bc0\u3002<br>Online edition in Traditional Chinese, covering all 7 chapters.</div>
  <div class="btn-row">
    <a class="btn primary" href="zh-tw/index.html">\u5728\u7dda\u700f\u89bd \u2192</a>
    {pdf_link("zh-tw", "FTC-Team-32477-Origin-Quick-Start-Guide-2026-08-01-zh-tw.pdf")}
  </div>
</div>""")

    lang_cards.append(f"""
<div class="lang-card en-us">
  <h3>English (US)</h3>
  <div class="lang-name">English \u00b7 United States</div>
  <div class="desc">The online edition in English (US) for international outreach and exchange, covering all 7 chapters.<br>\u9762\u5411\u56fd\u9645\u4ea4\u6d41\u7684\u82f1\u8bed\uff08\u7f8e\u5f0f\uff09\u5728\u7ebf\u7248\u672c\uff0c\u542b\u5168\u90e8 7 \u4e2a\u7ae0\u8282\u3002</div>
  <div class="btn-row">
    <a class="btn primary" href="en-us/index.html">Read Online \u2192</a>
    {pdf_link("en-us", "FTC-Team-32477-Origin-Quick-Start-Guide-2026-08-01-en-us.pdf")}
  </div>
</div>""")

    lang_cards.append(f"""
<div class="lang-card fr">
  <h3>Fran\u00e7ais</h3>
  <div class="lang-name">French \u00b7 France</div>
  <div class="desc">\u9762\u5411\u6cd5\u8bed\u4f7f\u7528\u8005\u7684\u6cd5\u6587\u5728\u7ebf\u7248\u672c\uff0c\u542b\u5168\u90e8 7 \u4e2a\u7ae0\u8282\u3002<br>\u00c9dition en ligne en fran\u00e7ais, couvrant l'ensemble des 7 chapitres.</div>
  <div class="btn-row">
    <a class="btn primary" href="fr/index.html">Consulter en ligne \u2192</a>
    {pdf_link("fr", "FTC-Team-32477-Origin-Quick-Start-Guide-2026-08-01-fr.pdf")}
  </div>
</div>""")

    cards_html = "\n".join(lang_cards)

    # 章节列表（三语言名称对照）
    chapters = [
        ("index", "前言", "前言", "Preface"),
        ("member", "队员须知", "隊員須知", "Team Essentials"),
        ("modeling", "建模设计", "建模設計", "Modeling & Design"),
        ("build", "结构建造", "結構建造", "Hardware & Build"),
        ("programming", "程序设计", "程式設計", "Programming"),
        ("outreach", "外部联络", "外部聯絡", "Outreach & PR"),
        ("afterword", "后记", "後記", "Afterword"),
    ]
    chapter_items = []
    for num, (key, zh_cn, zh_tw, en) in enumerate(chapters, start=1):
        chapter_items.append(
            f'<li><span class="num">{num}</span>'
            f'<span class="name">{zh_cn}</span>'
            f'<span class="names">{zh_tw} · {en}</span></li>'
        )
    chapters_html = "\n".join(chapter_items)

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FTC 32477 Origin \u5feb\u901f\u5165\u95e8\u6307\u5357 | Quick Start Guide</title>
<link rel="icon" href="images/basic/icon_team_logo.ico" type="image/x-icon">
<link rel="shortcut icon" href="images/basic/icon_team_logo.ico" type="image/x-icon">
<style>{HOMEPAGE_CSS}</style>
</head>
<body>

<div class="hero">
  <img class="hero-logo" src="images/basic/team_logo.png" alt="32477 Origin Team Logo">
  <div class="badge">TEAM 32477 ORIGIN</div>
  <h1>FIRST\u00ae Tech Challenge<br>\u5feb\u901f\u5165\u95e8\u6307\u5357</h1>
  <div class="subtitle">Quick Start Guide \u00b7 \u62d2\u7edd\u91cd\u590d\u9020\u8f6e\u5b50 \u00b7 Refuse to Reinvent the Wheel</div>
</div>

<div class="container">

  <section id="about">
    <h2>\u9879\u76ee\u6982\u51b5 <span class="en">About Us</span></h2>
    <div class="about-simple">
      <p class="about-line">
        <span class="tag-label">\u961f\u4f0d</span>
        <span class="text">FTC Team 32477 Origin <span class="en">FIRST\u00ae Tech Challenge</span></span>
      </p>
      <p class="about-line">
        <span class="tag-label">\u5b66\u6821</span>
        <span class="text">\u4e2d\u56fd\u5317\u4eac\u5e02\u6d77\u6dc0\u533a \u00b7 \u5317\u4eac\u5341\u4e00\u5b9e\u9a8c\u4e2d\u5b66 <span class="en">Beijing National Day Experimental School, Haidian District, Beijing, China</span></span>
      </p>
      <p class="about-line">
        <span class="tag-label">\u5730\u5740</span>
        <span class="text">\u5317\u4eac\u5e02\u6d77\u6dc0\u533a\u592a\u5e73\u8def8\u53f7 \u00b7 \u90ae\u653f\u7f16\u7801 100039 <span class="en">No. 8 Taiping Road, Haidian District, Beijing 100039, China</span></span>
      </p>
      <p class="about-line">
        <span class="tag-label">\u6700\u65b0\u7248\u672c</span>
        <span class="text">2026\u5e748\u6708\u7b2c1\u7248 <span class="en">1st Edition \u00b7 August 2026</span></span>
      </p>
    </div>
  </section>

  <section id="languages">
    <h2>\u9009\u62e9\u8bed\u8a00 <span class="en">Choose Your Language</span></h2>
    <div class="lang-grid">
{cards_html}
    </div>
  </section>

  <section id="chapters">
    <h2>\u5185\u5bb9\u7ed3\u6784 <span class="en">Table of Contents</span></h2>
    <ul class="chapter-list">
{chapters_html}
    </ul>
  </section>

</div>

<footer>
  32477 Origin \u5feb\u901f\u5165\u95e8\u6307\u5357\u7f16\u5199\u5c0f\u7ec4 \u00b7 Editorial Team \u00b7 2026\u5e748\u6708
  <div class="legal">
    <p>Legal Notice: This guide is an independent publication of FTC Team 32477 Origin. Our team is not affiliated with, endorsed by, or sponsored by FIRST\u00ae (For Inspiration and Recognition of Science and Technology). FIRST\u00ae, FIRST\u00ae Robotics Competition, FRC\u00ae, FIRST\u00ae Tech Challenge, and FTC\u00ae are registered trademarks of FIRST. All team designs, code, and resources shared in this guide are provided by our team members and do not represent official FIRST materials.</p>
    <p>\u6cd5\u5f8b\u58f0\u660e\uff1a\u672c\u6307\u5357\u662f FTC 32477 Origin \u961f\u4f0d\u7684\u72ec\u7acb\u51fa\u7248\u7269\u3002\u672c\u961f\u4f0d\u4e0e FIRST\u00ae\uff08For Inspiration and Recognition of Science and Technology\uff09\u65e0\u96b6\u5c5e\u3001\u80cc\u4e66\u6216\u8d5e\u52a9\u5173\u7cfb\u3002FIRST\u00ae\u3001FIRST\u00ae Robotics Competition\u3001FRC\u00ae\u3001FIRST\u00ae Tech Challenge \u53ca FTC\u00ae \u5747\u4e3a FIRST \u7684\u6ce8\u518c\u5546\u6807\u3002\u672c\u6307\u5357\u4e2d\u5206\u4eab\u7684\u6240\u6709\u961f\u4f0d\u8bbe\u8ba1\u3001\u4ee3\u7801\u4e0e\u8d44\u6e90\u5747\u7531\u961f\u4f0d\u6210\u5458\u63d0\u4f9b\uff0c\u4e0d\u4ee3\u8868 FIRST \u5b98\u65b9\u6750\u6599\u3002</p>
  </div>
</footer>

</body>
</html>"""


# ============================================================
#  构建主流程
# ============================================================

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def build():
    """读取所有语言的 Markdown 文件并生成 HTML。"""
    print("=" * 56)
    print("  FTC 32477 Origin — 多语言快速入门指南构建工具")
    print("=" * 56)

    ensure_dir(DIST_DIR)

    total = 0
    for lang_key, lang in LANGUAGES.items():
        lang_src = os.path.join(SRC_DIR, lang_key)
        lang_dist = os.path.join(DIST_DIR, lang_key)
        ensure_dir(lang_dist)

        for page_key in PAGE_KEYS:
            md_path = os.path.join(lang_src, f"{page_key}.md")
            if not os.path.exists(md_path):
                print(f"  [警告] 源文件不存在: {md_path}")
                continue

            with open(md_path, "r", encoding="utf-8") as f:
                md_content = f.read()

            html_body, headings = parse_markdown(md_content)
            full_html = render_page(page_key, html_body, lang_key, headings)

            out_path = os.path.join(lang_dist, f"{page_key}.html")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(full_html)
            total += 1

        print(f"  [构建] {lang['label']} ({lang_key}) — {len(PAGE_KEYS)} 页")

    # 生成主页（语言选择落地页）
    homepage_html = render_homepage()
    with open(os.path.join(DIST_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(homepage_html)
    print("  [生成] index.html（语言选择主页，含 PDF 下载链接）")

    # 复制图片目录
    dist_images = os.path.join(DIST_DIR, "images")
    if os.path.exists(dist_images):
        shutil.rmtree(dist_images)
    if os.path.exists(IMAGES_DIR):
        shutil.copytree(IMAGES_DIR, dist_images)
        img_count = sum(
            len(files)
            for _, _, files in os.walk(IMAGES_DIR)
        )
        print(f"  [复制] images/ → dist/images/ ({img_count} 个文件)")
    else:
        ensure_dir(dist_images)
        print("  [提示] images/ 目录为空，可放置图片后重新构建")

    print("-" * 56)
    print(f"  构建完成! 共生成 {total} 个页面，输出目录: {shorten_path(DIST_DIR)}")
    print("=" * 56)


def shorten_path(path):
    home = os.path.expanduser("~")
    if path.startswith(home):
        return "~" + path[len(home):]
    return path


def watch():
    """监听文件变化并自动重新构建。"""
    file_hashes = {}

    def hash_file(path):
        try:
            with open(path, "rb") as f:
                return hashlib.md5(f.read()).hexdigest()
        except FileNotFoundError:
            return None

    def scan():
        changed = set()
        for lang_key in LANGUAGES:
            for page_key in PAGE_KEYS:
                path = os.path.join(SRC_DIR, lang_key, f"{page_key}.md")
                h = hash_file(path)
                if h != file_hashes.get(path):
                    file_hashes[path] = h
                    changed.add(f"{lang_key}/{page_key}")
        return changed

    for lang_key in LANGUAGES:
        for page_key in PAGE_KEYS:
            path = os.path.join(SRC_DIR, lang_key, f"{page_key}.md")
            file_hashes[path] = hash_file(path)

    build()
    print("\n  [监听] 正在监听 src/ 目录变化，按 Ctrl+C 退出...\n")

    try:
        while True:
            time.sleep(1.5)
            changed = scan()
            if changed:
                print(f"\n  检测到变化: {', '.join(sorted(changed))}")
                build()
                print("\n  [监听] 继续监听...\n")
    except KeyboardInterrupt:
        print("\n  已停止监听。")


if __name__ == "__main__":
    if "--watch" in sys.argv:
        watch()
    else:
        build()
