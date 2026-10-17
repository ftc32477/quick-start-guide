#!/usr/bin/env python3
"""编译工具扩展语法单元测试（无外部依赖，python3 -m unittest 可跑）。"""
import os
import re
import sys
import unittest

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
import build  # noqa: E402


def render(md, lang="zh-hans", page="programming"):
    fig_map = {}
    ctx1 = build.new_figure_context(lang, page, collect=True, fig_map=fig_map)
    build.parse_markdown(md, fig_ctx=ctx1)
    ctx2 = build.new_figure_context(lang, page, collect=False, fig_map=fig_map)
    html, headings = build.parse_markdown(md, fig_ctx=ctx2)
    return html, fig_map, ctx1, ctx2, headings


class ImageAttrTest(unittest.TestCase):
    def test_parse_attrs(self):
        item = build.parse_image_line(
            "![图注](../images/x.png){w=60% mh=8cm align=center #fig:hub}")
        self.assertEqual(item["alt"], "图注")
        self.assertEqual(item["src"], "../images/x.png")
        self.assertEqual(item["attrs"]["w"], "60%")
        self.assertEqual(item["attrs"]["mh"], "8cm")
        self.assertEqual(item["attrs"]["align"], "center")
        self.assertEqual(item["attrs"]["id"], "fig:hub")

    def test_plain_image(self):
        item = build.parse_image_line("![a](../images/a.png)")
        self.assertEqual(item["attrs"], {})
        self.assertIsNone(build.parse_image_line("文字 ![a](b.png) 文字"))

    def test_style_and_inline(self):
        html, *_ = render("![图](../images/x.png){w=420 mh=8cm}")
        self.assertIn("width:420", html)
        self.assertIn("max-height:8cm", html)
        self.assertIn("loading=\"lazy\"", html)

    def test_unknown_attr_ignored(self):
        attrs = build.parse_attr_text("widht=60% foo=bar w=50%")
        self.assertEqual(attrs, {"w": "50%"})


class FigureNumberTest(unittest.TestCase):
    def test_prefixes(self):
        self.assertEqual(build.figure_prefix("member", "zh-hans"), "1")
        self.assertEqual(build.figure_prefix("programming", "zh-hans"), "4")
        self.assertEqual(build.figure_prefix("preface", "zh-hans"), "序")
        self.assertEqual(build.figure_prefix("afterword", "zh-hans"), "后")
        self.assertEqual(build.figure_prefix("afterword", "en-us"), "Postscript")

    def test_labels_localized(self):
        html, favg, *_ = render("![A](../images/a.png)\n![B](../images/b.png)")
        self.assertEqual(favg, {})
        self.assertIn("图 4-1", html)
        self.assertIn("图 4-2", html)
        html_en, *_ = render("![A](../images/a.png)", lang="en-us")
        self.assertIn("Figure 4-1", html_en)

    def test_ids_and_refs(self):
        md = "见 [](#fig:hub)。\n\n![Hub](../images/a.png){#fig:hub}\n\n" \
             "![Power](../images/b.png){#fig:power}"
        html, favg, _c1, c2, _ = render(md)
        self.assertEqual(favg["fig:hub"], "图 4-1")
        self.assertEqual(favg["fig:power"], "图 4-2")
        self.assertIn('href="#fig:hub">图 4-1</a>', html)
        self.assertIn('id="fig:hub"', html)
        self.assertEqual(c2["warnings"], [])

    def test_missing_ref_warns(self):
        _html, _favg, _c1, c2, _ = render("见 [](#fig:none)")
        self.assertTrue(any("fig:none" in w for w in c2["warnings"]))


class LayoutTest(unittest.TestCase):
    def test_image_group_table(self):
        html, *_ = render("![A](../images/a.png)\n![B](../images/b.png)")
        self.assertIn('<table class="media-row media-cols-2"', html)
        self.assertEqual(html.count("<figure"), 2)

    def test_grid3(self):
        md = "::: grid 3\n![A](../images/a.png)\n![B](../images/b.png)\n" \
             "![C](../images/c.png)\n:::"
        html, *_ = render(md)
        self.assertIn("media-cols-3", html)

    def test_side(self):
        md = "::: side\n### 左栏\n文字。\n\n![右图](../images/a.png)\n:::"
        html, *_ = render(md)
        self.assertIn('<table class="media-side"', html)
        self.assertIn("side-text", html)
        self.assertIn("side-fig", html)

    def test_side_reverse(self):
        md = "::: side reverse 40\n文字。\n\n![图](../images/a.png)\n:::"
        html, *_ = render(md)
        self.assertIn("--side-img:40%", html)
        # reverse 时图片单元格在文字之前
        self.assertLess(html.index("side-fig"), html.index("side-text"))

    def test_keep_and_break(self):
        html, *_ = render("::: keep\n> [!warning] 提示\n:::\n\n::: break\n:::")
        self.assertIn('<div class="keep">', html)
        self.assertIn('<div class="page-break"', html)

    def test_internal_link_not_blank(self):
        html, *_ = render("[内部](#foo) [外部](https://example.com)")
        self.assertIn('href="#foo">内部</a>', html)
        self.assertIn('target="_blank"', html)


if __name__ == "__main__":
    unittest.main()
