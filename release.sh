#!/usr/bin/env bash
# FTC 32477 Origin 快速入门指南 — 发版脚本（半自动）
#
# 用法: ./release.sh <TAG> <NOTES_FILE>
#   例: ./release.sh v1.3.2 release-notes/v1.3.2.md
#
# 流程（与 README「八、发版流程」一致）:
#   构建 HTML + 七语言 PDF → 本地提交 → [确认] 打 tag 并推送
#   → [确认] 创建 Release 上传 PDF（随后才推送 dev，避免主页下载按钮暂时 404）
#   → 清理本地旧版 PDF → [确认] 合并 main 重建推送
# 推送/发布类步骤会逐项询问确认（保持"推送必须人工确认"的原则）。
# 说明：NOTES_FILE 若不在 release-notes/{TAG}.md，会在前置检查通过后归档一份到该位置。
set -euo pipefail

BASE="$(cd "$(dirname "$0")" && pwd)"
cd "$BASE"

TAG="${1:-}"
NOTES="${2:-}"

[ -n "$TAG" ] || { echo "用法: $0 <TAG> <NOTES_FILE>"; exit 1; }
[ -n "$NOTES" ] || { echo "用法: $0 <TAG> <NOTES_FILE>（Release 说明文件，参考既往英文风格）"; exit 1; }
[ -f "$NOTES" ] || { echo "说明文件不存在: $NOTES"; exit 1; }

BRANCH="$(git rev-parse --abbrev-ref HEAD)"
[ "$BRANCH" = "dev" ] || { echo "请在 dev 分支执行发版。"; exit 1; }
command -v gh >/dev/null || { echo "缺少 gh CLI（brew install gh）。"; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "gh 未登录（gh auth login）。"; exit 1; }
[ -z "$(git status --porcelain)" ] || { echo "工作区不干净，请先提交或清理。"; exit 1; }
git rev-parse "$TAG" >/dev/null 2>&1 && { echo "本地已存在 tag $TAG。"; exit 1; }

# 一致性校验：TAG 必须与 build.py 的 RELEASE_TAG / VERSIONS 顶部条目一致
python3 - "$TAG" <<'PY'
import re, sys
tag = sys.argv[1]
src = open("build.py", encoding="utf-8").read()
m = re.search(r'^RELEASE_TAG = "([^"]+)"', src, re.M)
release_tag = m.group(1) if m else ""
sys.path.insert(0, ".")
import build  # noqa: E402
top_tag = build.VERSIONS[0]["tag"] if build.VERSIONS else ""
if not (tag == release_tag == top_tag):
    raise SystemExit(
        f"[错误] 版本号不一致：参数 {tag} / RELEASE_TAG {release_tag} / VERSIONS[0] {top_tag}"
    )
print(f"[校验] 版本号一致：{tag}")
PY

# —— 归档 Release 说明（放在所有前置检查之后；源与目标相同时跳过 cp）——
mkdir -p release-notes
NOTES_ABS="$(cd "$(dirname "$NOTES")" && pwd)/$(basename "$NOTES")"
NOTES_DST="$BASE/release-notes/${TAG}.md"
if [ "$NOTES_ABS" = "$NOTES_DST" ]; then
    echo "（Release 说明已位于归档位置：release-notes/${TAG}.md）"
else
    cp "$NOTES" "$NOTES_DST"
    echo "（Release 说明已归档到 release-notes/${TAG}.md）"
fi

confirm() {
    read -r -p "$1 [y/N] " ans
    [[ "$ans" =~ ^[Yy]$ ]]
}

echo "==> [1/7] 构建 HTML 与七语言 PDF（请自查 dist/pdf 产物）"
python3 build.py
python3 build_pdf.py

LANG_COUNT="$(python3 -c 'import build; print(len(build.LANGUAGES))')"
PDF_COUNT="$(find dist/pdf -maxdepth 1 -name "FTC-Team-32477-Origin-Quick-Start-Guide-${TAG}-*.pdf" | wc -l | tr -d ' ')"
if [ "$PDF_COUNT" -ne "$LANG_COUNT" ]; then
    echo "[错误] dist/pdf 中 ${TAG} 的 PDF 数量为 ${PDF_COUNT}，应为 ${LANG_COUNT}（每语言一份），已中止。"
    exit 1
fi
echo "（PDF 数量校验通过：${PDF_COUNT} 份）"

echo "==> [2/7] 本地提交"
git add -A
if git diff --cached --quiet; then
    echo "（无变更，跳过提交）"
else
    git commit -m "发版 $TAG：构建产物与发版数据更新"
fi

echo "==> [3/7] 打 tag 并推送（tag 携带提交，源码压缩包即为当前代码）"
if confirm "创建 tag $TAG 并推送到 origin（tag 推送不可撤销）？"; then
    git tag "$TAG"
    git push origin "$TAG"
else
    echo "已跳过 tag 推送；本地未创建 tag。"; exit 1
fi

echo "==> [4/7] 创建 GitHub Release 并上传七语言 PDF"
if confirm "创建 GitHub Release $TAG 并公开上传 PDF？"; then
    if ! gh release create "$TAG" --title "$TAG" --notes-file "$NOTES" \
        "dist/pdf"/FTC-Team-32477-Origin-Quick-Start-Guide-"${TAG}"-*.pdf; then
        echo "[提示] tag 已推送但 Release 创建失败。修复后手工重试（不要重复推送 tag）："
        echo "       gh release create $TAG --title $TAG --notes-file $NOTES \"dist/pdf\"/*-${TAG}-*.pdf"
        exit 1
    fi
else
    echo "已跳过 Release 创建；tag 已推送，修复后请手工创建 Release。"; exit 1
fi

echo "==> [5/7] 推送 dev（Release 资产已就绪，主页下载按钮不会 404）"
if confirm "推送到 origin/dev？"; then
    git push origin dev
else
    echo "已跳过推送 dev。"; exit 1
fi

echo "==> [6/7] 清理本地旧版本 PDF（仅保留当前 $TAG）"
find dist/pdf -maxdepth 1 -name 'FTC-Team-32477-Origin-Quick-Start-Guide-*.pdf' \
    ! -name "*${TAG}-*.pdf" -delete

echo "==> [7/7] 合并 main 并重建推送"
if confirm "合并 dev → main、重建并推送 origin/main？"; then
    git checkout main
    if ! git merge dev -m "Merge dev into main for $TAG release"; then
        echo "合并冲突：dist 为生成产物，优先取 dev 版本后重建。"
        git checkout --theirs -- dist 2>/dev/null || git checkout HEAD -- dist
        git add -A
        git commit -m "Merge dev into main for $TAG release"
    fi
    python3 build.py
    git add -A
    if ! git diff --cached --quiet; then
        git commit -m "$TAG 发布：main 合并 dev 并重建（主页下载与历史版本页指向 $TAG Release）"
    fi
    git push origin main
    git checkout dev
else
    echo "已跳过 main 合并。"
fi

echo "完成。"
