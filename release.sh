#!/usr/bin/env bash
# FTC 32477 Origin 快速入门指南 — 发版脚本（半自动）
#
# 用法: ./release.sh <TAG> <NOTES_FILE>
#   例: ./release.sh v1.3.0 /path/to/release-notes.md
#
# 流程（与 README「八、发版流程」一致）:
#   构建 HTML + 六语言 PDF → 本地自动提交 → [确认] 推 dev → 打 tag → gh 建 Release 上传 PDF
#   → 清理本地旧版 PDF → [确认] 合并 main 重建推送
# 推送类步骤会逐项询问确认（保持"推送必须人工确认"的原则）。
set -euo pipefail

BASE="$(cd "$(dirname "$0")" && pwd)"
cd "$BASE"

TAG="${1:-}"
NOTES="${2:-}"

[ -n "$TAG" ] || { echo "用法: $0 <TAG> <NOTES_FILE>"; exit 1; }
[ -n "$NOTES" ] || { echo "用法: $0 <TAG> <NOTES_FILE>（Release 说明文件，参考既往英文风格）"; exit 1; }
[ -f "$NOTES" ] || { echo "说明文件不存在: $NOTES"; exit 1; }

mkdir -p release-notes
cp "$NOTES" "release-notes/${TAG}.md"
echo "（Release 说明已归档到 release-notes/${TAG}.md）"

BRANCH="$(git rev-parse --abbrev-ref HEAD)"
[ "$BRANCH" = "dev" ] || { echo "请在 dev 分支执行发版。"; exit 1; }
command -v gh >/dev/null || { echo "缺少 gh CLI（brew install gh）。"; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "gh 未登录（gh auth login）。"; exit 1; }
[ -z "$(git status --porcelain)" ] || { echo "工作区不干净，请先提交或清理。"; exit 1; }

confirm() {
    read -r -p "$1 [y/N] " ans
    [[ "$ans" =~ ^[Yy]$ ]]
}

echo "==> [1/7] 构建 HTML 与六语言 PDF（请自查 dist/pdf 产物）"
python3 build.py
python3 build_pdf.py

echo "==> [2/7] 本地提交"
git add -A
if git diff --cached --quiet; then
    echo "（无变更，跳过提交）"
else
    git commit -m "发版 $TAG：构建产物与发版数据更新"
fi

echo "==> [3/7] 推送 dev"
if confirm "推送到 origin/dev？"; then
    git push origin dev
else
    echo "已跳过推送 dev。"; exit 1
fi

echo "==> [4/7] 打 tag 并推送（先推 dev 再 tag，保证 Release 源码压缩包为最新代码）"
git tag "$TAG"
git push origin "$TAG"

echo "==> [5/7] 创建 GitHub Release 并上传六语言 PDF"
gh release create "$TAG" --title "$TAG" --notes-file "$NOTES" \
    "dist/pdf"/FTC-Team-32477-Origin-Quick-Start-Guide-"${TAG}"-*.pdf

echo "==> [6/7] 清理本地旧版本 PDF（仅保留当前 $TAG）"
find dist/pdf -maxdepth 1 -name 'FTC-Team-32477-Origin-Quick-Start-Guide-*.pdf' \
    ! -name "*${TAG}-*.pdf" -delete

echo "==> [7/7] 合并 main 并重建推送"
if confirm "合并 dev → main、重建并推送 origin/main？"; then
    git checkout main
    if ! git merge dev -m "Merge dev into main for $TAG release"; then
        echo "合并冲突：dist 为生成产物，取 dev 版本后重建。"
        git checkout --theirs -- dist
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
