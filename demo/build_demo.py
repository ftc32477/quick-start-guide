#!/usr/bin/env python3
"""构建语法示例页：输出 HTML 与 PDF（用于人工检查编译工具效果）。

用法:
    python3 demo/build_demo.py [输出目录]
默认输出到 /tmp/ftc-syntax-demo；会复制 dist/images 到输出目录供相对路径引用。
"""
import os
import shutil
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
import build  # noqa: E402
import build_pdf  # noqa: E402


def main():
    out = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else "/tmp/ftc-syntax-demo"
    demo_md = os.path.join(BASE, "demo", "syntax-demo.md")
    if not os.path.exists(demo_md):
        raise SystemExit(f"缺少示例源文件: {demo_md}")
    if not os.path.isdir(os.path.join(BASE, "dist", "images")):
        raise SystemExit("请先运行 python3 build.py 生成 dist/images")
    os.makedirs(os.path.join(out, "zh-hans"), exist_ok=True)
    # 复制图片（保留 ../images/ 相对引用）
    dst_images = os.path.join(out, "images")
    if os.path.exists(dst_images):
        shutil.rmtree(dst_images)
    shutil.copytree(os.path.join(BASE, "dist", "images"), dst_images)

    md = open(demo_md, encoding="utf-8").read()
    fig_map = {}
    ctx1 = build.new_figure_context("zh-hans", "member", collect=True, fig_map=fig_map)
    build.parse_markdown(md, fig_ctx=ctx1)
    ctx2 = build.new_figure_context("zh-hans", "member", collect=False, fig_map=fig_map)
    body, _headings = build.parse_markdown(md, fig_ctx=ctx2)
    for w in ctx1["warnings"] + ctx2["warnings"]:
        print(f"[图注警告] {w}")

    html = (
        '<!DOCTYPE html><html lang="zh-hans"><head><meta charset="utf-8">'
        f"<title>编译工具语法示例</title><style>{build.CSS}</style></head>"
        f"<body><main>{body}</main></body></html>"
    )
    html_path = os.path.join(out, "zh-hans", "syntax-demo.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[HTML] {html_path}（图注 {len(fig_map)} 个 id）")

    # 生成 PDF（复用 build_pdf 的 Chrome CDP 打印，A4 与正文一致页边距）
    chrome = build_pdf.find_chrome()
    if not chrome:
        print("[跳过] 未找到 Chrome/Edge，只输出 HTML")
        return
    proc, port = build_pdf.start_chrome(chrome)
    client = build_pdf.CDPClient(port)
    try:
        client.connect()
        client.navigate("file://" + html_path)
        pdf_path = os.path.join(out, "syntax-demo.pdf")
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
