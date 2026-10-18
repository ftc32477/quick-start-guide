#!/usr/bin/env python3
"""生成 v2.0.0 内容草稿预览（HTML + PDF），不进入正式构建。

用法:
    python3 build.py                    # 先生成 dist/images
    python3 drafts/build_draft.py [输出目录]
默认输出 /tmp/ftc-v2-draft。
"""
import os
import shutil
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
import build  # noqa: E402
import build_pdf  # noqa: E402

DRAFT_DIR = os.path.join(BASE, "drafts", "v2.0.0")
# (文件, 图注章号前缀, 标题)
PAGES = [
    ("operations.md", "6", "比赛与运营"),
    ("appendix.md", "A", "附录"),
]


def render_md(path, prefix, lang="zh-hans"):
    """渲染草稿页；返回 (html, warnings)。"""
    with open(path, encoding="utf-8") as f:
        md = f.read()
    fig_map = {}
    ctx_collect = build.new_figure_context(lang, "outreach", collect=True,
                                           fig_map=fig_map)
    ctx_collect["prefix"] = prefix
    build.parse_markdown(md, fig_ctx=ctx_collect)
    ctx_render = build.new_figure_context(lang, "outreach", collect=False,
                                          fig_map=fig_map)
    ctx_render["prefix"] = prefix
    html, _headings = build.parse_markdown(md, fig_ctx=ctx_render)
    warnings = ctx_collect["warnings"] + ctx_render["warnings"]
    return html, warnings


def main():
    out = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else "/tmp/ftc-v2-draft"
    lang_dir = os.path.join(out, "zh-hans")
    os.makedirs(lang_dir, exist_ok=True)

    dist_images = os.path.join(BASE, "dist", "images")
    if os.path.isdir(dist_images):
        dst_images = os.path.join(out, "images")
        if os.path.exists(dst_images):
            shutil.rmtree(dst_images)
        shutil.copytree(dist_images, dst_images)

    sections = []
    warnings = []
    for filename, prefix, title in PAGES:
        path = os.path.join(DRAFT_DIR, "zh-hans", filename)
        if not os.path.exists(path):
            print(f"[跳过] 缺少草稿: {path}")
            continue
        html, warns = render_md(path, prefix)
        warnings.extend(warns)
        sections.append(
            f'<section class="draft-section" data-title="{title}">{html}</section>')

    for w in warnings:
        print(f"[图注警告] {w}")

    extra_css = """
.draft-banner{
  background:#fff8e1;border:1px solid #f9a825;border-radius:8px;
  padding:10px 16px;margin:0 0 24px;font-size:13px;color:#6d4c00
}
.draft-section{padding-bottom:32px;border-bottom:1px dashed #ccc;margin-bottom:32px}
@media print{.draft-section + .draft-section{break-before:page;page-break-before:always}}
.draft-section:last-child{border-bottom:none}
"""
    html = (
        '<!DOCTYPE html><html lang="zh-hans"><head><meta charset="utf-8">'
        "<title>FTC 32477 v2.0.0 内容草稿预览</title>"
        f"<style>{build.CSS}{extra_css}</style></head><body><main>"
        '<div class="draft-banner">FTC 32477《快速入门指南》v2.0.0 内容草稿预览'
        "（2026-10-18，非正式发布；TODO 注释不显示在页面中）</div>"
        + "".join(sections) + "</main></body></html>"
    )
    html_path = os.path.join(lang_dir, "draft-preview.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    todo_count = html.count("<!-- TODO")
    print(f"[HTML] {html_path}（{len(sections)} 页，TODO 注释 {todo_count} 处）")

    chrome = build_pdf.find_chrome()
    if not chrome:
        print("[跳过] 未找到 Chrome/Edge，只生成 HTML")
        return
    proc, port = build_pdf.start_chrome(chrome)
    client = build_pdf.CDPClient(port)
    try:
        client.connect()
        client.navigate("file://" + html_path)
        pdf_path = os.path.join(out, "draft-preview.pdf")
        client.print_to_pdf(pdf_path)
        print(f"[PDF] {pdf_path}")
    finally:
        try:
            client.close()
            proc.terminate()
            proc.wait(timeout=5)
        except Exception:
            proc.kill()


if __name__ == "__main__":
    main()
