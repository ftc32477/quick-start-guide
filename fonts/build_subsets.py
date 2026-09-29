#!/usr/bin/env python3
"""
FTC 32477 Origin 快速入门指南 — PDF 字体子集生成工具

按各语言 PDF 的实际用字，从 fonts/source/ 的全量开源字体生成
fonts/subsets/ 下的静态子集（TTF），并输出 coverage.json 供
build_pdf.py 构建时校验用字覆盖。

常规队员无需运行本脚本（子集已入库）；仅当指南新增用字、构建报
"用字超出字体子集覆盖"时，由维护者运行：

    pip3 install fonttools
    python3 fonts/build_subsets.py           # 源字体已在 fonts/source/ 时
    python3 fonts/build_subsets.py --fetch   # 先自动下载全量源字体（约 150MB）

字体来源与许可见主 README「PDF 字体（开源子集）」章节；许可证文本在
fonts/licenses/。
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import urllib.request

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS_DIR = os.path.join(BASE_DIR, "fonts")
SOURCE_DIR = os.path.join(FONTS_DIR, "source")
SUBSET_DIR = os.path.join(FONTS_DIR, "subsets")

sys.path.insert(0, BASE_DIR)
import build_pdf as bp  # noqa: E402

GF = "https://raw.githubusercontent.com/google/fonts/main/ofl"
LXGW = "https://github.com/lxgw/LxgwWenKai/releases/download/v1.522"
LXGWTC = "https://github.com/lxgw/LxgwWenkaiTC/releases/download/v1.522"

# 全量源字体下载清单（官方仓库，均为 OFL 1.1）
SOURCES = {
    "NotoSerifSC[wght].ttf": f"{GF}/notoserifsc/NotoSerifSC%5Bwght%5D.ttf",
    "NotoSansSC[wght].ttf": f"{GF}/notosanssc/NotoSansSC%5Bwght%5D.ttf",
    "NotoSerifTC[wght].ttf": f"{GF}/notoseriftc/NotoSerifTC%5Bwght%5D.ttf",
    "NotoSansTC[wght].ttf": f"{GF}/notosanstc/NotoSansTC%5Bwght%5D.ttf",
    "NotoSerifKR[wght].ttf": f"{GF}/notoserifkr/NotoSerifKR%5Bwght%5D.ttf",
    "NotoSansKR[wght].ttf": f"{GF}/notosanskr/NotoSansKR%5Bwght%5D.ttf",
    "NotoSans[wdth,wght].ttf": f"{GF}/notosans/NotoSans%5Bwdth%2Cwght%5D.ttf",
    "LXGWWenKai-Regular.ttf": f"{LXGW}/LXGWWenKai-Regular.ttf",
    "LXGWWenKai-Medium.ttf": f"{LXGW}/LXGWWenKai-Medium.ttf",
    "LXGWWenKaiTC-Regular.ttf": f"{LXGWTC}/LXGWWenKaiTC-Regular.ttf",
    "LXGWWenKaiTC-Medium.ttf": f"{LXGWTC}/LXGWWenKaiTC-Medium.ttf",
    "Tinos-Regular.ttf": f"{GF}/tinos/Tinos-Regular.ttf",
    "Tinos-Bold.ttf": f"{GF}/tinos/Tinos-Bold.ttf",
    "Tinos-Italic.ttf": f"{GF}/tinos/Tinos-Italic.ttf",
    "Tinos-BoldItalic.ttf": f"{GF}/tinos/Tinos-BoldItalic.ttf",
}

# (源文件, 可变轴设置, 输出子集, 字体族, 子族, 用字集合键)
FACES = [
    # 简体：思源宋体 / 思源黑体 / 霞鹜文楷（子集改名 Origin Kai）
    ("NotoSerifSC[wght].ttf", {"wght": 400}, "NotoSerifSC-Regular.ttf", "Noto Serif SC", "Regular", "zh-hans"),
    ("NotoSerifSC[wght].ttf", {"wght": 700}, "NotoSerifSC-Bold.ttf", "Noto Serif SC", "Bold", "zh-hans"),
    ("NotoSansSC[wght].ttf", {"wght": 400}, "NotoSansSC-Regular.ttf", "Noto Sans SC", "Regular", "zh-hans"),
    ("NotoSansSC[wght].ttf", {"wght": 700}, "NotoSansSC-Bold.ttf", "Noto Sans SC", "Bold", "zh-hans"),
    ("LXGWWenKai-Regular.ttf", None, "OriginKaiSC-Regular.ttf", "Origin Kai SC", "Regular", "zh-hans"),
    ("LXGWWenKai-Medium.ttf", None, "OriginKaiSC-Bold.ttf", "Origin Kai SC", "Bold", "zh-hans"),
    # 繁体
    ("NotoSerifTC[wght].ttf", {"wght": 400}, "NotoSerifTC-Regular.ttf", "Noto Serif TC", "Regular", "zh-hant"),
    ("NotoSerifTC[wght].ttf", {"wght": 700}, "NotoSerifTC-Bold.ttf", "Noto Serif TC", "Bold", "zh-hant"),
    ("NotoSansTC[wght].ttf", {"wght": 400}, "NotoSansTC-Regular.ttf", "Noto Sans TC", "Regular", "zh-hant"),
    ("NotoSansTC[wght].ttf", {"wght": 700}, "NotoSansTC-Bold.ttf", "Noto Sans TC", "Bold", "zh-hant"),
    ("LXGWWenKaiTC-Regular.ttf", None, "OriginKaiTC-Regular.ttf", "Origin Kai TC", "Regular", "zh-hant"),
    ("LXGWWenKaiTC-Medium.ttf", None, "OriginKaiTC-Bold.ttf", "Origin Kai TC", "Bold", "zh-hant"),
    # 韩语
    ("NotoSerifKR[wght].ttf", {"wght": 400}, "NotoSerifKR-Regular.ttf", "Noto Serif KR", "Regular", "ko"),
    ("NotoSerifKR[wght].ttf", {"wght": 700}, "NotoSerifKR-Bold.ttf", "Noto Serif KR", "Bold", "ko"),
    ("NotoSansKR[wght].ttf", {"wght": 400}, "NotoSansKR-Regular.ttf", "Noto Sans KR", "Regular", "ko"),
    ("NotoSansKR[wght].ttf", {"wght": 700}, "NotoSansKR-Bold.ttf", "Noto Sans KR", "Bold", "ko"),
    # 西文（Times New Roman 的度量兼容开源替代）与通用无衬线
    ("Tinos-Regular.ttf", None, "Tinos-Regular.ttf", "Tinos", "Regular", "latin"),
    ("Tinos-Bold.ttf", None, "Tinos-Bold.ttf", "Tinos", "Bold", "latin"),
    ("Tinos-Italic.ttf", None, "Tinos-Italic.ttf", "Tinos", "Italic", "latin"),
    ("Tinos-BoldItalic.ttf", None, "Tinos-BoldItalic.ttf", "Tinos", "Bold Italic", "latin"),
    ("NotoSans[wdth,wght].ttf", {"wdth": 100, "wght": 400}, "NotoSans-Regular.ttf", "Noto Sans", "Regular", "latin"),
    ("NotoSans[wdth,wght].ttf", {"wdth": 100, "wght": 700}, "NotoSans-Bold.ttf", "Noto Sans", "Bold", "latin"),
]

_LANG_TEXT = {}


def lang_text(lang):
    if lang not in _LANG_TEXT:
        _LANG_TEXT[lang] = bp.required_text(lang)
    return _LANG_TEXT[lang]


def is_cjk(ch):
    o = ord(ch)
    return (0x2E80 <= o <= 0x9FFF or 0x3000 <= o <= 0x303F
            or 0xF900 <= o <= 0xFAFF or 0xFE10 <= o <= 0xFE4F
            or 0xFF00 <= o <= 0xFFEF or 0x20000 <= o <= 0x2FA1F)


def is_hangul(ch):
    o = ord(ch)
    return (0x1100 <= o <= 0x11FF or 0x3130 <= o <= 0x318F
            or 0xA960 <= o <= 0xA97F or 0xAC00 <= o <= 0xD7AF
            or 0xD7B0 <= o <= 0xD7FF)


def han_union():
    """六语言文本中的全部汉字（供简/繁/韩 CJK 字体覆盖跨语言注记）。"""
    s = set()
    for lang in bp.LANGUAGES:
        s |= {c for c in lang_text(lang) if is_cjk(c)}
    return "".join(sorted(s))


def latin_union():
    """六语言文本中的全部非 CJK/谚文字符（供 Tinos / Noto Sans 覆盖）。"""
    s = set()
    for lang in bp.LANGUAGES:
        s |= {c for c in lang_text(lang) if not is_cjk(c) and not is_hangul(c)}
    return "".join(sorted(s))


def charset(key):
    if key == "zh-hans":
        return lang_text("zh-hans") + han_union()
    if key == "zh-hant":
        return lang_text("zh-hant") + han_union()
    if key == "ko":
        return lang_text("ko") + han_union()
    if key == "latin":
        return latin_union()
    raise ValueError(key)


def rename(font, family, subfamily):
    """统一改写 name 表（避免实例化残留 ExtraLight 等名称）。"""
    ps = family.replace(" ", "") + "-" + subfamily.replace(" ", "")
    full = family if subfamily == "Regular" else f"{family} {subfamily}"
    name = font["name"]
    name.names = []
    for nid, val in ((1, family), (2, subfamily), (3, ps + ";subset"),
                     (4, full), (6, ps), (16, family), (17, subfamily)):
        name.setName(val, nid, 3, 1, 0x409)   # Windows Unicode
        name.setName(val, nid, 1, 0, 0)       # Mac Roman（名称均为 ASCII）


def fix_style_flags(font, subfamily):
    """按子族修正字重/斜体标记（霞鹜文楷 Medium 用作 Bold 时尤其重要）。"""
    bold = "Bold" in subfamily
    italic = "Italic" in subfamily
    os2 = font["OS/2"]
    os2.usWeightClass = 700 if bold else 400
    if bold:
        os2.fsSelection |= 0x20
    else:
        os2.fsSelection &= ~0x20
    if italic:
        os2.fsSelection |= 0x01
    else:
        os2.fsSelection &= ~0x01
    if bold or italic:
        os2.fsSelection &= ~0x40
    else:
        os2.fsSelection |= 0x40
    mac = font["head"].macStyle
    font["head"].macStyle = (mac | 0x1) if bold else (mac & ~0x1)
    font["head"].macStyle = (font["head"].macStyle | 0x2) if italic \
        else (font["head"].macStyle & ~0x2)


def to_ranges(codepoints):
    ranges = []
    for cp in codepoints:
        if ranges and cp == ranges[-1][1] + 1:
            ranges[-1][1] = cp
        else:
            ranges.append([cp, cp])
    return ranges


def _download(url, dest):
    """优先用系统 curl（兼容 macOS 自带 Python 无根证书的情况）。"""
    curl = shutil.which("curl")
    if curl:
        subprocess.run(
            [curl, "-fL", "--retry", "3", "--max-time", "900",
             "-o", dest + ".part", url],
            check=True,
        )
        os.replace(dest + ".part", dest)
        return
    req = urllib.request.Request(url, headers={"User-Agent": "ftc-fonts/1.0"})
    with urllib.request.urlopen(req, timeout=600) as resp, \
            open(dest, "wb") as out:
        shutil.copyfileobj(resp, out)


def fetch_sources():
    os.makedirs(SOURCE_DIR, exist_ok=True)
    for name, url in SOURCES.items():
        dest = os.path.join(SOURCE_DIR, name)
        if os.path.exists(dest):
            print(f"  [已有] {name}")
            continue
        print(f"  [下载] {name} …")
        _download(url, dest)


def build_one(face):
    from fontTools.ttLib import TTFont

    source, axes, output, family, subfamily, charset_key = face
    src_path = os.path.join(SOURCE_DIR, source)
    if not os.path.exists(src_path):
        raise SystemExit(f"[错误] 缺少源字体 {src_path}\n"
                         f"       请运行 python3 fonts/build_subsets.py --fetch")
    font = TTFont(src_path)
    if axes and "fvar" in font:
        from fontTools.varLib.instancer import instantiateVariableFont
        instantiateVariableFont(font, axes, inplace=True)
    rename(font, family, subfamily)
    fix_style_flags(font, subfamily)

    from fontTools import subset
    opts = subset.Options()
    opts.hinting = False
    sub = subset.Subsetter(options=opts)
    sub.populate(text=charset(charset_key))
    sub.subset(font)

    out_path = os.path.join(SUBSET_DIR, output)
    font.save(out_path)
    return output, to_ranges(sorted(font.getBestCmap().keys()))


def main():
    parser = argparse.ArgumentParser(description="生成 PDF 字体子集")
    parser.add_argument("--fetch", action="store_true",
                        help="先下载缺失的全量源字体到 fonts/source/")
    args = parser.parse_args()

    try:
        import fontTools  # noqa: F401
    except ImportError:
        raise SystemExit("缺少 fonttools，请先运行: pip3 install fonttools")

    if args.fetch:
        print("[1/3] 下载全量源字体：")
        fetch_sources()

    os.makedirs(SUBSET_DIR, exist_ok=True)
    coverage = {}
    total = 0
    print("[2/3] 生成子集：")
    for face in FACES:
        output, ranges = build_one(face)
        size = os.path.getsize(os.path.join(SUBSET_DIR, output))
        total += size
        coverage[output] = ranges
        print(f"  {output:32s} {size / 1024:7.1f} KB  "
              f"({sum(e - s + 1 for s, e in ranges)} 字符)")
    print(f"  合计：{total / 1024 / 1024:.2f} MB")

    expected = {f[3] for f in bp.FONT_FACES}
    assert set(coverage) == expected, (
        f"子集与 build_pdf.FONT_FACES 不一致：缺 {expected - set(coverage)}，"
        f"多 {set(coverage) - expected}"
    )
    cov_path = os.path.join(SUBSET_DIR, "coverage.json")
    with open(cov_path, "w", encoding="utf-8") as f:
        json.dump(coverage, f, ensure_ascii=False, sort_keys=True)
    print(f"[3/3] 覆盖清单：{os.path.relpath(cov_path, BASE_DIR)}")


if __name__ == "__main__":
    main()
