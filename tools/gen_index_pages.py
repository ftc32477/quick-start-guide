#!/usr/bin/env python3
"""从已生成的 zh-hans PDF 提取插图/表格的印刷页码，写入 data/index-pages-zh-hans.json。

用法（内容或版式变化后按顺序执行）：
    python3 build.py --channel dev
    python3 build_pdf.py --lang zh-hans
    python3 tools/gen_index_pages.py
    python3 build.py --channel dev
    python3 build_pdf.py --lang zh-hans

说明：页码映射依赖当前 PDF 排版；未重新生成时会显示“—”，不要手工猜页码。
"""
import json
import pathlib
import re
import sys

try:
    from pypdf import PdfReader
except ImportError:
    sys.exit("需要 pypdf：pip3 install pypdf")

BASE = pathlib.Path(__file__).resolve().parent.parent
PDF = BASE / "dist/pdf/FTC-Team-32477-Origin-Quick-Start-Guide-v1.5.1-zh-hans.pdf"
APPENDIX = BASE / "dist/zh-hans/appendix.html"
OUT = BASE / "data/index-pages-zh-hans.json"


def norm(text):
    return re.sub(r"\s+", "", text)


def printed_page(text):
    lines = [x.strip() for x in text.strip().split("\n") if x.strip()]
    if lines:
        m = re.match(r"^([0-9]{1,3}|[IVXLCDM]{1,6})$", lines[-1])
        if m:
            return m.group(1)
    m = re.findall(r"[—–-]\s*([0-9]{1,3}|[IVXLCDM]{1,6})\s*[—–-]", text)
    return m[-1] if m else None


def main():
    html = APPENDIX.read_text(encoding="utf-8")
    m = re.search(r'<section class="book-index".*?</section>', html, re.S)
    if not m:
        sys.exit("appendix 中没有 book-index 区块；请先运行 python3 build.py")
    section = m.group(0)
    fig_labels = [x.strip() for x in re.findall(
        r'<a[^>]*>(图\s*[^<]+?)\s*<span class="idx-gap"', section)]
    tbl_labels = [x.strip() for x in re.findall(
        r'<a[^>]*>(表\s*[^<]+?)\s*<span class="idx-gap"', section)]

    reader = PdfReader(PDF)
    pages = [norm(p.extract_text() or "") for p in reader.pages]

    def find(label):
        needle = norm(label)
        allow_roman = label.startswith(("表 序", "图 序"))
        roman_fallback = None
        for idx, text in enumerate(pages):
            if "插图索引" in text and "表格索引" in text and len(text) < 3000:
                continue
            if needle not in text:
                continue
            page = printed_page(reader.pages[idx].extract_text() or "")
            if not page:
                continue
            if page.isdigit():
                return page
            if allow_roman and roman_fallback is None:
                roman_fallback = page
        return roman_fallback

    figures = {label: find(label) for label in fig_labels}
    tables = {label: find(label) for label in tbl_labels}
    figures = {k: v for k, v in figures.items() if v}
    tables = {k: v for k, v in tables.items() if v}
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps({"figures": figures, "tables": tables},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"写入 {OUT}: 插图 {len(figures)} 条，表格 {len(tables)} 条")
    missing = [x for x in fig_labels if x not in figures] + [x for x in tbl_labels if x not in tables]
    if missing:
        print("未定位：", missing)


if __name__ == "__main__":
    main()
