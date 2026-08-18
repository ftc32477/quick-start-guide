# FTC 32477 Origin 快速入门指南 — 项目文档

本项目将 Markdown 源文件转换为多语言 HTML 网站与 PDF 文档。

**本文档分为两部分，面向两组不同的维护人员：**

- **第一部分：构建与导出维护** —— 面向维护 HTML 网站与生成 PDF 的组员
- **第二部分：内容撰写规范** —— 面向撰写 `.md` 源文件的组员

---

## 项目架构

```
ftc_quick_start_guide/
├── src/                       # Markdown 源文件（内容组在此编辑）
│   ├── zh-hans/                 # 简体中文源文件
│   │   ├── preface.md         # 前言
│   │   ├── member.md          # 队员须知
│   │   ├── modeling.md        # 建模设计
│   │   ├── build.md           # 结构建造
│   │   ├── programming.md     # 程序设计
│   │   ├── outreach.md        # 外部联络
│   │   └── afterword.md       # 后记
│   ├── zh-hant/                 # 繁体中文源文件（同 zh-hans 结构）
│   ├── en-us/                 # 英文（美式）源文件（同 zh-hans 结构）
│   ├── fr/                    # 法语源文件（同 zh-hans 结构）
│   ├── es/                    # 西班牙语源文件（同 zh-hans 结构）
│   └── ko/                    # 韩语源文件（同 zh-hans 结构）
├── images/                    # 图片资源（构建时自动复制到 dist/images/）
│   ├── basic/                 # 通用资源（六语言共用）
│   │   ├── icon_team_logo.ico # 标签栏图标（favicon）
│   │   └── team_logo.png      # 队徽（侧边栏/顶栏/主页英雄区）
│   └── afterword/             # 后记专用图片（大合照等）
├── dist/                      # 生成产物（每次构建都会覆盖，勿直接编辑）
│   ├── index.html             # 根门户（语言选择落地页，仿 wikipedia.org）
│   ├── zh-hans/                 # 简体中文网站（主页 + 7 页 + 历史版本页）
│   ├── zh-hant/                 # 繁体中文网站（主页 + 7 页 + 歷史版本頁）
│   ├── en-us/                 # 英文（美式）网站（Home + 7 pages + Version History）
│   ├── fr/                    # 法语网站（Accueil + 7 pages + Historique des versions）
│   ├── es/                    # 西班牙语网站（Inicio + 7 páginas + Historial de versiones）
│   ├── ko/                    # 韩语网站（홈 + 7 페이지 + 버전 기록）
│   ├── images/                # 图片（自动复制）
│   └── pdf/                   # PDF 产物（本地生成、不入库；正式版作为 GitHub Release 资产发布）
│       ├── FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.2-zh-hans.pdf  # 简体中文完整指南（封面+正文+封底）
│       ├── FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.2-zh-hant.pdf  # 繁体中文完整指南
│       ├── FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.2-en-us.pdf  # 英文（美式）完整指南
│       ├── FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.2-fr.pdf     # 法语完整指南
│       ├── FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.2-es.pdf     # 西班牙语完整指南
│       └── FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.2-ko.pdf     # 韩语完整指南
├── build.py                   # HTML 构建脚本
├── build_pdf.py               # PDF 导出脚本
└── README.md                  # 本文档
```

> 本项目托管于主仓库 `ftc32477/quick-start-guide`；推送后由 GitHub Actions 自动把 `dist/` 同步为发布仓库 `ftc32477/ftc32477.github.io` 的 `docs/` 目录，即线上站点 https://ftc32477.github.io/docs/ 。详见第一部分"八、发布到 GitHub Pages"。

---

# 第一部分：构建与导出维护（HTML / PDF 组员）

## 一、使用的工具与依赖

本项目使用了以下工具，均已安装完毕，无需重复安装（重装环境时参照安装）：

| 工具 | 用途 |
|------|------|
| Python 3 | 运行构建脚本（`build.py`、`build_pdf.py`） |
| Google Chrome / Microsoft Edge | 无头模式渲染 HTML 页面为 PDF（PDF 导出核心） |
| pip3 | 安装以下 Python 依赖 |
| websocket-client | 与 Chrome 调试端口（CDP）通信，实现页眉页脚模板、封面渲染 |
| pypdf | PDF 合并、读取页面、页脚覆盖层盖印、目录内部超链接注解（Link） |
| reportlab | 在 PDF 上绘制页脚文字（内置 STSong-Light/MSung-Light 中文字体，无需字体文件） |

```bash
pip3 install websocket-client pypdf reportlab
```

## 二、快速开始

### 构建 HTML 网站

```bash
python3 build.py              # 一次性构建
python3 build.py --watch      # 监听模式（src/*.md、images/ 与 build.py 变化自动重建；build.py 变更时自动重启监听）
```

### 导出 PDF

```bash
python3 build_pdf.py                # 导出全部六种语言的 PDF
python3 build_pdf.py --lang en-us   # 仅导出英文（美式）
python3 build_pdf.py --page member  # 仅导出"队员须知"页面
python3 build_pdf.py --rebuild      # 先重建 HTML 再导出 PDF
```

- 完整导出（不带 `--page`）在合并成功后会自动删除各语言的单页 PDF，`dist/pdf/` 下只保留六语言合并版。
- `--page` 用于内容调试：只生成指定页的单页 PDF（含页眉页脚），不删除。
- `dist/pdf/` 已加入 `.gitignore` **不入库**，仅本地生成用于自查纠错；正式发布的 PDF 上传为 GitHub Release 资产（见"八、发布到 GitHub Pages"）。

### 链接行为约定

- **站内导航（同一标签页）**：侧边栏/顶栏返回根门户、页面切换、语言切换、锚点跳转均为当前标签页内跳转；侧边栏首项"主页"指向该语言主页。
- **PDF 下载（新标签页）**：各语言主页的 PDF 按钮使用 `target="_blank"`，点击后在新标签页打开 GitHub Release 资产 PDF（浏览器内置预览器），从预览器下载。

## 三、PDF 结构（多语言自动本地化）

每个语言的合并指南 `FTC-Team-32477-Origin-Quick-Start-Guide-{RELEASE_TAG}-{lang}.pdf`（{lang} 为 zh-hans / zh-hant / en-us / fr / es / ko）结构如下：

1. **封面**：深色渐变背景（135°），内容放大并位于黄金分割点（内容中心 ≈ 38.2vh）；居中队徽、队伍徽章、"FIRST® Tech Challenge"、指南名（本地化）、学校，组团信息行距较大；底部居中"语言版本 / 版次日期"**两行**（如"简体中文版"+"2026年8月第3版·第1次修订"，位置略上移）
2. **封二（版权页）**：白底排版、内容置于页面下部，含完整书名、**版次（2026年8月第3版·第2次修订）**、**版本号（v1.2.2）**、**发布日期（2026年8月17日）**、语言版本、主编/编写人员、出品方与地址，以及完整法律声明；数据取自 `VERSIONS` 最新已发布条目，随发版自动更新
3. **前言**：罗马数字页脚（仅当前页码，如 I、II，不标总页码）
4. **目录**：前言之后、队员须知之前，两级结构——第一级为章节，第二级为各章 h2 小标题（更深层级不收录）；每行标注起始页码（前言用罗马数字、正文用阿拉伯数字），整行均为 PDF 内部超链接，点击跳转到对应页；目录页脚沿用罗马数字
5. **正文页**（队员须知起）：
   - 页眉：左侧"FTC 32477 Origin 快速入门指南"（随语言本地化），右侧当前章回标题
   - 页脚：居中"— X —"式页码（仅当前页码），**从队员须知第一页重新从 1 计数**
6. **封三（资源与更新页）**：在线版本、历史版本、开源仓库、意见反馈四个渠道链接
7. **封底**：与封面**镜像对称**（渐变方向翻转 135°→45°、光斑位置镜像），居中队徽（宽度为纸面宽度的 0.618 倍）+ 右下角"语言版本 / 版次日期"**两行**（位置略偏左上）

封面、封二、封三与封底均不编页码、不进目录。

单页 PDF（`pdf/{lang}/{page}.pdf`）仅由 `--page` 参数生成（同样含页眉页脚，页码按该 PDF 自身计），供内容调试使用；完整导出结束后自动删除。

**页面布局参数：** A4 纸（210×297mm）；上下页边距各 2.54cm（1in）、左右各 3.18cm（1.25in）；页眉页脚字号均为 11pt（文字高度一致）；封面与封底边距为 0，封二为满版渲染、内边距与正文页边距一致（上下 1in、左右 1.25in）。

**中文排版规范（仅中文版生效）：** 正文每段首行缩进 2 字符（`text-indent:2em`，通过 `html[lang]` 区分）；一级标题前空约两行、二级标题前空约一行、三级标题前空约 0.7 行。英文版按英文书写规范排版。

### 页脚连续编号与目录超链接的实现

- Chrome CDP 的 `footerTemplate` 只能统计**单次打印任务内**的页码，分章渲染再合并会导致"共 X 页"错误。
- 因此正文页渲染时**只带页眉不带页脚**，合并后由 reportlab 在每页**盖印页脚**（pypdf `merge_page` 叠加层）：
  - 前言/目录：罗马数字（I、II、III…），仅当前页码
  - 正文：阿拉伯数字"— 1 —"式（仅当前页码）
  - 封面、封二、封三与封底不编号
- **目录页与各章起始页**：章节页码按各章 PDF 页数累计计算；h2 小项页码用**字号检测**定位（实测 h2 打印字号 Tf=24.0pt，检测 23–25pt 的行）——不依赖文本匹配，规避 PDF 字体子集产生的异体字形（如 ⻔/⼊）导致 NFKC 也无法归一的问题。
- **超链接注入**：合并后从目录页**提取实际文本行位置**。注意 pypdf 的 `tm` 是未变换坐标，必须按 `x = cm[0]*tm[4] + cm[2]*tm[5] + cm[4]`、`y = cm[1]*tm[4] + cm[3]*tm[5] + cm[5]` 换算为页面坐标（Chrome 正文流 cm≈[0.75,0,0,-0.75,90,769.92]），并按上下边距过滤页眉/页脚/盖印层；逐行构造矩形；`/Dest` 用 `writer._add_object` 取得目标页的**间接引用**手工构造注解（pypdf 的 `Link` 注解会把页码以纯数字写入 /Dest，不符合 PDF 规范，多数阅读器无法正确跳转）。
- **目录页页边距与宽度**：目录 HTML 中不得出现 `@page { margin: 0 }`（那是封面/封二/封底专用的满版设置），否则目录内容会铺满整页、与页眉页脚重叠、跨页连续；标题用 `padding-top` 代替 `margin-top` 防止外边距折叠把标题顶到页边。目录容器水平 padding 为 **0.45in**——注意 CDP 页边距（1.25in）与容器 padding 会**叠加**，调整宽度时按"页面宽度 − 2×(页边距 + padding)"计算实际行宽。
- 中文字体使用 reportlab 内置 CID 字体：简体 STSong-Light（UniGB-UCS2-H）、繁体 MSung-Light（UniCNS-UCS2-H），无需字体文件。
- **繁体页脚字形坑（重要）**：reportlab 默认把 MSung-Light（Adobe-CNS1 繁体字体）硬编码映射到简体 CMap `UniGB-UCS2-H`，繁体专用字形（如"頁"）在该 CMap 中无对应，页脚中会渲染为空白。`build_pdf.py` 的 `_stamp_engine()` 中已将映射修正为 `UniCNS-UCS2-H`，切勿删除该修正。

## 四、门户与语言主页设计

### 根门户（dist/index.html，由 `render_portal()` 生成）

仿 wikipedia.org 的语言选择落地页，结构极简：

- **英雄区**：队徽 + 队伍徽章 + 指南标题 + 标语（拒绝重复造轮子 · Refuse to Reinvent the Wheel）。
- **语言选择**：六张卡片（简体中文 / 繁體中文 / English (US) / Français / Español / 한국어），卡片整体为链接 → `{lang}/index.html`（各语言主页）；最多两列排布（宽屏两列、窄屏 ≤600px 单列）。
- **页脚**：编辑组署名 + 中英双语法律声明。
- 门户不含 PDF 下载与历史版本入口（都在各语言主页内）。

### 各语言主页（dist/{lang}/index.html，由 `render_lang_homepage()` 生成）

选择语言后进入的本地化落地页，复用指南页外壳（侧边栏/顶栏/语言切换），侧边栏导航为"主页 + 7 章"。内容分节：

1. **英雄区**：队徽 + 徽章 + 指南名（本地化）+ 标语（本地化）
2. **项目概况**：队伍 / 学校 / 地址 / 最新版本（本地化）
3. **下载**：说明文字（离线版本、无需联网即可阅读、可打印）+ 本语言 PDF 下载按钮 → GitHub Release 资产（自动取 `VERSIONS` 中最新已发布版本的本语言资产）
4. **内容结构**：7 章链接列表（本地化，链到各章页面）
5. **历史版本入口**：说明文字 + 按钮 → 本语言 `versions.html`
6. **法律声明**：本地化单语

- 语言切换下拉：主页之间互相切换（`../{lk}/index.html`）；侧边栏"主页"项指向本语言主页；品牌点击返回根门户
- 各语言主页文案在 `build.py` 的 `LANG_HOME_TEXTS` 中维护

## 五、响应式布局策略

正文宽度分三档平滑过渡，无跳变：

| 屏幕宽度 | 行为 |
|----------|------|
| 宽屏（>1160px） | 内容固定约 900px 宽，居中于侧边栏右侧；留白随宽度**连续**收窄 |
| 中屏（769–1160px） | 留白归零后内容随屏宽缩小，侧边栏保留 |
| 窄屏（≤768px） | 侧边栏折叠，顶栏 + 菜单按钮展开抽屉；内容全宽 |

实现要点（`build.py` 中 main 的 CSS）：

- 使用 `box-sizing:content-box` + `width: calc(100vw - sidebar - 2*pad)` 配合 `max-width: calc(900px - 2*pad)` 封顶——**只用普通 calc，不用 min()**。
- 居中偏移量 `max(0px, (100vw - sidebar - 900px)/2)` 随屏宽连续归零，实现平滑过渡；`margin-left` 先声明 `var(--sidebar-w)` 作为回退。
- **兼容性坑（重要）**：部分 Chrome 版本对嵌套在自定义属性中的 `min()/max()/clamp()`（含 `vw` 单位）存在布局计算 bug——宽度会被算成 0，导致**正文空白而侧边栏正常**（Edge/Firefox 正常）。因此 main 的布局一律使用普通 calc + 级联回退声明，`clamp`/`min`/`max` 仅作为增强层，且都带有前置回退值。
- 窄屏抽屉宽度 `min(280px, 84vw)`，顶栏品牌文字自动省略号截断，另设 `≤420px` 极限档进一步缩小字号内边距。
- 表格在窄屏下负边距突破容器（`margin-left:-18px` 技巧）保证滚动顺畅。

## 六、导航与视觉组件（HTML 维护）

### 语言切换行为

- **侧边栏**：品牌区下方为下拉选项栏（简体中文 / 繁體中文 / English (US) / Français），选择后跳转到**当前页面**的对应语言版本（如 `zh-hans/member.html` → `../en-us/member.html`）。采用下拉栏而非按钮排列是为了**节省侧边栏空间给目录**。
- **移动端顶栏**：下拉选项栏（`<select>`）同样显示全称，切换即跳转。
- 页面标题格式：`{页面名}｜{站点名}`（如 `队员须知｜FTC 32477 Origin 快速入门指南`）。
- 侧边栏导航标题、页脚、`<title>` 均随语言自动本地化。

### 侧边栏二级目录

- 当前页面的 **h2/h3 标题**自动生成锚点 ID，并以缩进子项形式出现在侧边栏该页标题之下。
- 只有切换到该页时子项才显示（如进入"建模设计"后出现"基本资料""环境配置""建模设计要点"）。
- 点击子项平滑滚动到对应标题，`scroll-margin-top` 防止被固定顶栏遮挡（移动端加留白 64px）。

### 队徽与标签栏图标

- **标签栏图标**：`images/basic/icon_team_logo.ico` 自动注入所有页面（含主页）的 `<link rel="icon">`。
- **队徽**：`images/basic/team_logo.png` 显示在侧边栏标题区上方、移动端顶栏品牌左侧、主页英雄区顶部。点击侧边栏队徽同样返回主页。
- 替换图标：直接覆盖 `images/` 中同名文件后重新构建即可。

### 返回主页

- 侧边栏标题区（队徽 + 队伍名 + 品牌名）与移动端顶栏品牌标题均为**可点击链接**，指向 `../index.html`（根门户）。
- 悬停侧边栏标题有浅色背景反馈。

### SEO 与无障碍

- 所有页面（含门户）均含 `<meta name="description">` 与 og:/twitter: 社交分享 meta（og:image 为线上队徽绝对地址），描述文案在 `build.py` 的 `LANG_HOME_TEXTS[lang]["meta_desc"]` 维护。
- 语言下拉与移动端菜单按钮的 `aria-label` 随语言本地化（`LANGUAGES[lang]["lang_label"]` / `"menu_label"`）；菜单按钮带 `aria-controls` 与 `aria-expanded`（开合时由 JS 同步更新）。

## 七、打印样式与踩坑记录

### Chrome CDP 连接要点

- 启动参数需含 `--remote-debugging-port={port}`、`--remote-allow-origins=*`、独立的 `--user-data-dir`
- 新版 Chrome 拒绝未授权的 WebSocket 来源（403），`--remote-allow-origins=*` 为必填
- 通过 `http://127.0.0.1:{port}/json` 获取页面目标的 WebSocket 地址
- 打印参数：`printBackground:true`（保留深色封面）、`marginTop/Bottom:0.7in`、`marginLeft/Right:0.75in`（预留页眉页脚空间）、封面/封二/封底边距为 0
- 打印前滚动页面触发 `loading="lazy"` 图片加载

### 移动端媒体查询泄漏坑（重要）

**现象**：PDF 中表格宽度异常撑满、左侧字符被裁切。

**原因**：Chrome 无头模式打印时视口宽度（US Letter 约 739px）低于 768px 断点，导致 `@media(max-width:768px)` 的规则（如 `.table-wrap{margin-left:-18px;width:calc(100%+36px)}`）泄漏进打印渲染。

**对策**：`@media print` 中必须用 `!important` 显式覆盖所有移动端规则：

- `.table-wrap` 强制 `margin:0; width:100%`
- `html,body` 强制 `display:block; width:100%`（消除 flex 影响）
- `main` 强制 `box-sizing:border-box; margin:0; padding:0; width:100%`
- 锁定桌面排版值（标题字号、卡片内边距等），保证 PDF 与桌面视图一致

### 超长链接导致整页缩放坑（重要）

**现象**：某一部分（如建模设计整章）所有元素等比缩小，与其余章节字号不一致。

**原因**：超长不可断行的 URL（如 Onshape 应用商店链接）超出可打印宽度，Chrome 打印时为容纳它把**整页内容等比缩放**（PDF 内容流中 `cm` 矩阵从 0.75 变为约 0.54，字号 Tf 数值不变，肉眼看到的却是整章缩小）。

**对策**：链接必须允许任意位置断行——全局 `a{overflow-wrap:anywhere}`，并在 `@media print` 中 `a{overflow-wrap:anywhere !important}` 防媒体查询泄漏。验证方法：用 pypdf 的 `extract_text(visitor_text=...)` 检查各页 `cm` 矩阵比例是否一致（正常为 0.75）。

### 表格打印规则

- `table-layout:fixed` + `width:100%` —— 表格宽度严格限制在页面内
- `word-break:normal` + `overflow-wrap:break-word` —— 普通单词以词为单位换行（不切断单词）；仅当单个超长词/URL 超出单元格宽度时才在任意位置切断，防止触发整页缩放
- 打印时缩小单元格内边距（6px 8px）与字号（12px）
- `tr{page-break-inside:avoid}` —— 行不跨页截断

### 打印隐藏

- 侧边栏、顶栏、遮罩层在打印时 `display:none`，正文全宽单栏
- 卡片阴影去除、边框保留，Hero 反转为白底黑字保证打印效果

## 八、发布到 GitHub Pages

构建产物通过 GitHub Actions **自动发布**到 **https://ftc32477.github.io/docs/**。发布仓库全程由云端维护，无需手动操作。

### 文件流转逻辑

```
本地工作区（src/*.md、images/）
        │
        ▼ ① 构建（python3 build.py）
dist/（HTML 网站；dist/pdf/ 本地生成但不入库）
        │
        ▼ ② 提交 + 推送（git commit 本地自动；git push 人工确认后执行）
主仓库 ftc32477/quick-start-guide
        │
        ├─ main 分支 ──────────────► ③ Actions 同步 dist/ → docs/（正式站点）
        └─ dev 分支 ───────────────► ③ Actions 同步 dist/ → docs/dev/（开发预览站）
                                          │
                                          ▼ ④ GitHub Pages 自动部署
                                    线上站点 https://ftc32477.github.io/docs/
                                    预览站点 https://ftc32477.github.io/docs/dev/
```

- ① 本地构建：生成根门户 + 六语言"主页 + 7 页 + 历史版本页"共 55 个 HTML（需 Python 依赖，见"一、使用的工具与依赖"）；`build_pdf.py` 生成的 PDF 留在本地自查纠错，不入库
- ② 提交推送：每次修改完成后自动 `git commit` 到本地；经人工审查给出指示后才 `git push`，换机迁移只需 clone 主仓库
- ③ 云端同步：Actions 把 dist 整体同步为发布仓库对应目录（先清空再复制，避免残留旧文件；无变化时自动跳过提交）。**main → docs/（正式站点）、dev → docs/dev/（开发预览站）**
- ④ 站点生效：推送后约 1–2 分钟

**双分支分工：**

| 分支 | 用途 | 线上位置 |
|------|------|----------|
| `main` | 稳定发布线：只在新版本发布时从 dev 合并，线上内容阶段性更新 | https://ftc32477.github.io/docs/ |
| `dev` | 持续开发线：日常所有修改提交到这里，同事随时 clone/pull 同步 | https://ftc32477.github.io/docs/dev/（预览站） |

**版本号规则（SemVer + 版次混合）：** Git tag 与 PDF 文件名采用 SemVer（`v主.次.修`），版权页采用"第 N 版 + 日期"（**大改版或新增语言版本时版次 +1**，其余情况仅日期随新）。

| 改动类型 | 示例 | SemVer | 版权页 |
|---------|------|--------|--------|
| 大改版：章节重排/新增整章/整体重写 | 建模设计章全新扩写 | 主版本 +1 → v2.0.0 | 第4版 |
| 新增语言版本：全书新语言译本 | 新增西班牙语（Español）版（v1.1.0 先例）、韩语（한국어）版（v1.2.0 先例） | 次版本 +1 → v1.3.0 | 第4版 |
| 常规更新：新增小节/附录/新页面 | 新增《工具清单》附录 | 次版本 +1 → v1.3.0 | 第3版（日期随新） |
| 勘误：错别字/样式/小修正 | 人名与专有名词加注修正（v1.2.1 先例）、封面排版与工程化（v1.2.2 先例） | 修订 +1 → v1.2.3 | 第3版·第3次修订 |
| 开发中 | — | v1.3.0-preview | （仅预览站） |

**发版流程（每次一版）：**

1. 在 dev 定稿全部内容
2. 按版本号规则确定新版本号，同步更新 `build.py`（`RELEASE_TAG` 常量、`VERSIONS` 列表顶部追加该版本条目（tag/PDF 文件名/name/changes 需六语言填写）并把 status 改为 `released`、**`date` 填当日实际发布日期（YYYY-MM-DD）**）与 README 中的版本描述；合并 PDF 文件名由 `RELEASE_TAG` 自动生成，版权页数据取自 `VERSIONS`；**侧边栏页脚、语言主页"最新版本"、PDF 封面/封底日期均自动取自 `VERSIONS`，无需另行修改**；唯一需手工同步的是各语言 `afterword.md` 末行落款版次（六处）
3. 本地运行 `build_pdf.py` 生成 6 份 PDF（新文件名）并自查
4. 推送 dev → 打 tag → 创建新 Release（tag 如 `v1.2.3`）并上传 6 份 PDF 作为资产（**先推 dev 再打 tag**，保证 Release 源码压缩包为最新代码）；Release 说明文本同时存入 `release-notes/{tag}.md` 入库留档
5. dev 合并入 main 后**在 main 上重新运行 `python3 build.py`**（历史页自动隐藏 preview 条目）并提交 → 正式站点自动更新，主页下载链接指向新 Release
6. **发布后核对发布日期**：GitHub Release 页面显示的发布时间应与 `VERSIONS` 中该版本 `date` 一致（历史版本页展示该日期、封二取自该日期）；如不一致，立即修正 `VERSIONS` 日期、重新运行 `build.py` 与 `build_pdf.py`，并用 `gh release upload <TAG> <PDF...> --clobber` 原地替换 Release 资产

> 步骤 3–5 可用 `./release.sh <TAG> <NOTES_FILE>` 半自动执行（推送类步骤逐项询问确认）。另有 `check-dist.yml` 工作流：每次推送自动重跑 `build.py` 校验 `dist/` 与源码同步，未构建即推送会导致 Actions 失败。

### 历史版本页（{lang}/versions.html）

- **六语言各一份**（zh-hans / zh-hant / en-us / fr / es / ko），复用指南页外壳（侧边栏/顶栏/抽屉）；语言下拉与指南页一致：切换到**历史版本页的对应语言版本**（`versions.html` → `../en-us/versions.html`）；主页入口默认进入 `zh-hans/versions.html`
- 数据来源为 `build.py` 顶部 `VERSIONS` 列表：tag、发布日期（ISO 格式，页面按语言本地化展示）、`name`/`changes` 六语言字段、六语言 PDF 资产文件名；卡片 PDF 按钮指向 GitHub Release 资产，按钮只标注语言名（如"简体中文"），行首"下载："标签说明用途
- 默认倒序（最新在前），正文顶部可切换正序；左侧边栏为版本号锚点，点击平滑滚动跳转
- 历史页不保留过去版本的网页版（在线正文只有现版），卡片仅提供 PDF 下载
- `status: "preview"` 条目仅在 dev 分支构建时显示（带"预览"徽标、无 PDF 按钮），正式构建自动隐藏

### 借助的工具

| 环节 | 工具 |
|------|------|
| 本地构建 | Python 3 + `build.py` / `build_pdf.py`（Chrome 无头打印、websocket-client、pypdf、reportlab） |
| 版本控制 | Git（主仓库为唯一编辑入口，main/dev 双分支） |
| PDF 托管 | GitHub Releases（每版 PDF 作为 Release 资产，主页下载链接指向资产 URL） |
| 云端同步 | GitHub Actions（`ubuntu-latest` 运行器，公共仓库免费） |
| 跨仓库推送 | Fine-grained Personal Access Token（存为主仓库 Secret `PAGES_TOKEN`） |
| 站点托管 | GitHub Pages（发布仓库 docs/ 与 docs/dev/） |

### 密钥信息（重要）

- **Secret 名**：`PAGES_TOKEN`（位置：主仓库 Settings → Secrets and variables → Actions）
- **PAT 名称**：`make-ftc-quick-start-guide-to-github-io`（Fine-grained personal access token）
- **归属**：组织 `ftc32477` 名下
- **权限**：对发布仓库 `ftc32477/ftc32477.github.io` 的 Contents 写入权限
- **到期时间**：**2027-08-14（周六）**；到期后自动发布会失败，需提前重新生成 PAT 并更新主仓库 Secret

### 何时需要更新

| 场景 | 操作 |
|------|------|
| 修改指南内容 | 改 `src/` 下的 .md（在 dev 分支）→ 本地构建 → 自动提交 → 人工审查后推送 dev（开发预览站自动更新） |
| 更换工作电脑 | `git clone https://github.com/ftc32477/quick-start-guide.git` 即可，无需其他配置 |
| PAT 到期（2027-08-14 前） | 重新生成 PAT → 更新主仓库 `PAGES_TOKEN` Secret |
| 发布新版本 | 按"发版流程"执行：更新版本日期与 Release 链接 → 生成 PDF → 创建 Release 上传资产 → dev 合并 main |
| 自动发布失败排查 | 查看主仓库 Actions 页签运行日志；权限问题通常表现为推送被拒（403），检查 PAT 与 Secret |

**注意：**

- **本地自动提交、云端手动推送**：每次修改完成后自动 `git commit` 到本地仓库（`git push` 之前本地历史保留在本地）；从本地到主仓库的推送必须由人审查后给出明确指示才执行，**绝不接入自动推送**——本地的更新通常是大量细小改动，还可能包含需要更正的错误，只有确认内容无误后才能推送到云端。云端 Actions 只负责第二步（主仓库 → 发布仓库）的自动同步
- **2026-08 历史重写**：dist/pdf 已用 git filter-repo 从全部历史中剔除（仓库瘦身）；持有旧 clone 的同事需删除后重新 `git clone`，旧 clone 直接 push 会被拒绝
- 旧的本机发布仓库克隆（`ftc32477.github.io/`）不再需要，可留作紧急备用
- 不要直接在 GitHub 网页端修改发布仓库内容，一切以主仓库的 dist 为准

---

# 第二部分：内容撰写规范（.md 内容组员）

## 一、文本流转逻辑（重要）

本项目所有文本的流转方向是**单向的**，顺序如下，不可颠倒：

```
① 简体中文 .md（src/zh-hans/）        ← 唯一的编辑源头
        │
        ▼ 翻译/本地化
② 繁體中文 .md（src/zh-hant/）
   English (US) .md（src/en-us/）
   Français .md（src/fr/）
   Español .md（src/es/）
   한국어 .md（src/ko/）
        │
        ▼ 构建（python3 build.py）
③ HTML 网站（dist/index.html 根门户 + dist/zh-hans/、dist/zh-hant/、dist/en-us/、dist/fr/、dist/es/、dist/ko/ 各语言主页与页面）
        │
        ▼ 导出（python3 build_pdf.py）
④ PDF 文档（dist/pdf/，仅本地自查，不入库；正式版上传 GitHub Release）
        │
        ▼ 发布（见第一部分"八、发布到 GitHub Pages"）
⑤ GitHub Pages 网站（https://ftc32477.github.io/docs/ 根门户；各语言主页 /{lang}/index.html）
```

**规则：**

1. **一切内容修改必须从 `src/zh-hans/` 下的简体中文 .md 文件开始**。简体中文版是内容的事实标准（source of truth）。
2. 简体中文版定稿后，再同步翻译到 `src/zh-hant/`（繁体中文）、`src/en-us/`（English (US)）、`src/fr/`（Français）、`src/es/`（Español）和 `src/ko/`（한국어）。
3. 构建脚本只做**单向转换**（.md → .html → .pdf），**不支持**从 HTML 或 PDF 反向生成 .md。
4. 不要直接编辑 `dist/` 下的 HTML 或 PDF——它们每次构建都会被覆盖。如需重新生成产物，请联系 HTML/PDF 维护组员运行构建脚本。
5. 修改内容后由维护组员依次运行：
   ```bash
   python3 build.py       # ③ 生成六语言 HTML（含各语言主页与历史版本页）
   python3 build_pdf.py   # ④ 生成六语言 PDF
   ```

**外部素材的整合方式：**
- 会议记录、培训录音、旧版资料等外部素材，一律以现有指南为核心**取其精华**，不得推翻重来。
- 整合时先归类到对应章节（结构建造/程序设计/外部联络等），在 zh-hans 版定稿后再翻译。

## 二、多语言维护

### 语言命名规范

| 目录 | 显示名称 | 说明 |
|------|----------|------|
| zh-hans | 简体中文 | 简体中文（大陆用语） |
| zh-hant | 繁體中文 | 繁体中文（台湾正体用语，如程式設計、網路、雷射切割；人名附注简体原名，如 付修齊（付修齐）） |
| en-us | English (US) | 美式英语，**目录名必须为 en-us**（与 `en` 区分，明确美式变体） |
| fr | Français | 法语（法国），正式 vous 语体，遵循法语排版规范（« guillemets »、双标点前不换行空格等） |
| es | Español | 西班牙语（西班牙），正式/无人称语体（usted 与无人称句式，避免 tú），遵循西语排版规范（« » 引号、¿ ¡ 疑问感叹号等） |
| ko | 한국어 | 韩语（韩国），正式 합쇼체 语体（-합니다）；中国人名采用汉字读音并附注汉字原名（如 부수제(付修齐)） |

- 语言代码统一采用 **BCP 47 脚本代码**：简体为 `zh-hans`、繁体为 `zh-hant`（不用区域代码 `zh-cn`/`zh-tw`），西班牙语为 `es`（不用 `es-es`），韩语为 `ko`（不用 `ko-kr`），同时作用于目录名、语言键、HTML `lang`、PDF 文件名与线上网址路径。

- 语言切换 UI **必须显示全称**：简体中文 / 繁體中文 / English (US) / Français / Español / 한국어，不使用简写。
- 放不下时采用**下拉选项栏**（侧边栏与移动端顶栏均为下拉栏）。

### 人名与专有名词标注规范（全语言通用）

为消除翻译歧义，各译本对真实人名与特殊物名一律**附注原名**（原名用来源语言书写，供对照查阅）；译文本身已精准无歧义时可不加注：

| 场景 | 规则 | 示例 |
|------|------|------|
| 真实人名（拼音类译本 en-us/fr/es） | 拼音后附注汉字原名 | `Fu Xiuqi (付修齐)` |
| 真实人名（繁体中文版 zh-hant） | 繁体后附注简体原名；繁简同形者不加注 | `付修齊（付修齐）`；杜星洲 不加注 |
| 真实人名（韩语版 ko） | 汉字读音后附注汉字原名 | `부수제(付修齐)` |
| 专有物名（平台/产品/出版物等） | 译文或通用罗马名后附注来源语言原名 | `KIRIN (麒麟)`、`Bilibili (哔哩哔哩)`、韩语版 `빌리빌리(哔哩哔哩)` |
| 简体/繁体中文版中的外来译名 | 译名后附注来源语言原名 | `结构体（Part Studio）`、`构建（Build）`、`建置（Build）` |

- 该原则**双向适用**：简体/繁体中文版中源自其他语言的译名同样附注来源语言原名（如 Onshape 界面 `结构体（Part Studio）`）；源自中文的名称在中文版中即为原名，无需处理；其他语言之间互相引用时同理。
- 若译文为通用标准译名且无歧义（如 Git 的"克隆"、打印失败术语"炒面/spaghetti"），可不加注。
- 人物名单（后记全队成员、封二主编/编写人员）与正文出现处均按同一规则加注。

### 页面清单（page key 六语言对照）

| 文件名 | 简体中文 | 繁體中文 | English (US) | Français | Español | 한국어 |
|--------|----------|----------|---------|---------|---------|--------|
| （index.html，由 `render_lang_homepage` 生成） | 主页 | 首頁 | Home | Accueil | Inicio | 홈 |
| preface.md | 前言 | 前言 | Preface | Préface | Prefacio | 머리말 |
| member.md | 队员须知 | 隊員須知 | Team Essentials | Essentiels de l'équipe | Esenciales del equipo | 팀원 필수사항 |
| modeling.md | 建模设计 | 建模設計 | Modeling & Design | Modélisation & Conception | Modelado y diseño | 모델링 및 설계 |
| build.md | 结构建造 | 結構建造 | Hardware & Build | Matériel & Construction | Hardware y construcción | 하드웨어 및 제작 |
| programming.md | 程序设计 | 程式設計 | Programming | Programmation | Programación | 프로그래밍 |
| outreach.md | 外部联络 | 外部聯絡 | Outreach & PR | Sensibilisation & Relations publiques | Divulgación y relaciones públicas | 아웃리치 및 대외 홍보 |
| afterword.md | 后记 | 後記 | Afterword | Postface | Epílogo | 후기 |
| versions.html | 历史版本 | 歷史版本 | Version History | Historique des versions | Historial de versiones | 버전 기록 |

## 三、Markdown 语法参考

本构建工具支持以下 Markdown 语法。请按照此文档规范编写 `src/` 下的 `.md` 源文件。

### 标题

使用 `#` 表示标题，支持 1–6 级。

```markdown
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
```

**效果：** 一级标题用于页面主标题（每个 `.md` 文件开头的第一个 `#`）。二级标题用于大章节，三级标题用于小节，四级标题用于细分类目，以此类推。**h2/h3 会自动出现在侧边栏二级目录中，h4 及更深层级不收录。**

**用途：** 组织文档结构，构建页面层级。

### 段落

连续的文字行组成一个段落，段落之间用空行分隔。

```markdown
这是第一段文字。

这是第二段文字。
```

**用途：** 撰写正文内容。

### 粗体、斜体、粗斜体

```markdown
**粗体** — 用于强调关键词
*斜体* — 用于次要强调或书名
***粗斜体*** — 用于强烈强调
```

**效果：**

- `**粗体**` → **粗体**
- `*斜体*` → *斜体*
- `***粗斜体***` → ***粗斜体***

**用途：** `**粗体**` 用于强调重要术语、关键词；`*斜体*` 用于次要标记或引用名称。

> 注意：`_下划线_` 写法**不支持**，请使用 `*星号*`。

### 行内代码

```markdown
使用 `code` 标记行内代码。
```

**效果：** 使用 `code` 标记行内代码。

**用途：** 标记文件名、命令、代码片段、路径等。例如：`BNDES-FTC`、`192.168.3.1`、`..\Bambu Studio\`。

### 代码块

使用三个反引号包裹多行代码。

    ```
    这是多行
    代码块
    ```

**效果：** 渲染为深色背景的代码样式块。

**用途：** 展示多行命令、代码示例或需要保持原始格式的文本。

### 链接

```markdown
[链接文字](https://example.com/)
```

**效果：** [链接文字](https://example.com/)

**用途：** 引用外部资源、下载地址、官方文档等。所有外部链接会自动在新标签页打开。

### 图片

```markdown
![图片描述](images/photo.png)
```

**效果：** 在页面中插入图片。

**用途：** 在文档中插入照片、截图、示意图等。先将图片放入项目根目录的 `images/` 文件夹（建议按用途分子目录，如 `basic/`、`afterword/`），构建时会自动复制到 `dist/images/`，六语言页面共用。

**路径注意：** 语言页面位于 `dist/{lang}/` 子目录中，Markdown 中的相对路径需以 `../images/` 开头（如 `../images/afterword/photo.jpg`）。

> 图片也支持行内写法：`文字 ![图标](../images/basic/icon.png) 文字`，可以穿插在段落中。

### 并排图片（图片组）

**连续多行**图片语法（中间无空行、无其他内容）会自动合并为一个横向排布的图片组，窄屏（≤600px）时自动改为纵向单列：

```markdown
![大合照（2025年12月19日）](../images/afterword/group_photo_20251219.jpg)
![大合照（2026年5月28日）](../images/afterword/group_photo_20260528.jpg)
```

- 两张并排各占约一半宽度，三张及以上自动折行。
- 图片的 `[]` 描述文字会渲染为图片下方的说明文字（图注）。
- 单张图片独占一行宽度。
- PDF 打印时保持并排且不跨页截断。

### 引用

```markdown
> 这是一段引用文字。
```

**效果：** 渲染为带红色左边框、浅色背景的引用块。

**用途：** 用于重要提示、注意事项、警告信息等。例如：安装警告、管理员备注。

**类型化引用（三种样式）：** 在引用块第一行的 `>` 后紧跟类型标记，可渲染为不同颜色的引用块：

```markdown
> [!info] 这是引用材料。
> [!warning] 这是警告信息。
> [!danger] 这是需要严格关注的事项。
```

| 标记 | 样式 | 用途 |
|------|------|------|
| `> [!info]` | 蓝色左边框 + 浅蓝背景 | 引用材料、参考资料、补充说明 |
| `> [!warning]` | 黄色左边框 + 浅黄背景 | 警告信息、常见坑点 |
| `> [!danger]` | 红色左边框 + 浅红背景 | 需要严格关注的事项、安全要求 |
| （无标记） | 红色左边框 + 浅红背景 | 一般性提示、注意事项 |

- 类型标记只写在**第一行**，后续内容继续用 `>` 续行；标记后可紧跟正文，也可换行书写。
- 未知标记（如 `[!xxx]`）会被当作普通引用正文处理。
- 各类型仅以颜色区分，不带文字标签。

### 无序列表

```markdown
- 项目一
- 项目二
- 项目三
```

或使用 `*` 或 `+`：

```markdown
* 项目一
* 项目二
+ 项目三
```

**效果：** 渲染为带圆点的列表。

**用途：** 罗列无顺序关系的条目，如工具清单、注意事项、应用列表等。

### 嵌套列表

列表内可以嵌套子列表（有序、无序可以互相嵌套），只需在子列表项前增加缩进（2 个空格即可）：

```markdown
- 电子邮箱（推荐使用 @gmail.com 或 @outlook.com）
  - 创建 Gmail 账号：https://support.google.com/mail/answer/56256
  - 创建 Outlook 账号：https://outlook.live.com/
- GitHub
- Onshape
```

```markdown
1. 打开官网并单击"Sign up"
   - 注册期间，系统会要求验证电子邮件地址
   - 建议将国家/地区选择为"美国"
2. 等待管理员邀请
```

**效果：** 子列表缩进显示在父列表项下方。

**用途：** 表达层级关系，如分类下的细分条目、步骤中的补充说明。

### 有序列表

```markdown
1. 第一步
2. 第二步
3. 第三步
```

**效果：** 渲染为带数字编号的列表。

**用途：** 用于操作流程、安装步骤等需要按顺序执行的说明。

**引用块打断不重置编号：** 在步骤之间插入引用块（含 `> [!info]`、`> [!warning]` 等类型化引用）后，后续步骤会自动接续编号（渲染为 `<ol start>`），无需手工调整序号：

```markdown
1. 第一步
2. 第二步

> [!info] 补充说明。

3. 第三步（自动显示为 3，不会重新从 1 开始）
```

### 表格

```markdown
| 列一 | 列二 | 列三 |
|------|------|------|
| 数据1 | 数据2 | 数据3 |
| 数据4 | 数据5 | 数据6 |
```

**效果：** 渲染为具有表头深色背景、斑马纹行的表格。

**用途：** 展示对比信息、规格参数、材料特性等结构化数据。

**对齐方式（支持但建议使用默认左对齐）：**

```markdown
| 左对齐 | 居中 | 右对齐 |
|:-------|:----:|-------:|
| 内容   | 内容 | 内容   |
```

### 水平分割线

```markdown
---
```

**效果：** 渲染为一条灰色水平线。

**用途：** 分隔不同主题的内容块。

### 右对齐行

行首以 `-->` 开头，该行内容右对齐显示（支持行内粗体/斜体/链接等标记）：

```markdown
--> *32477 Origin 快速入门指南编写小组 · 2026年8月*
```

**用途：** 落款、署名等需要靠右的内容（如前言落款）。

### 注意事项

1. **空行很重要：** 不同元素之间必须用空行分隔，否则可能会被错误地合并为段落。
2. **缩进：** 列表项可以通过缩进实现嵌套，子列表项缩进 2 个空格即可。
3. **嵌套列表：** 支持嵌套列表（列表内再套列表），有序与无序列表可以互相嵌套。
4. **HTML 标签：** 除换行标签 `<br>`（用于标题或段落内的显式换行，如三行排版的前言标题）外，不要在 Markdown 中混入其他原始 HTML 标签，可能会破坏渲染结果。
5. **文件编码：** 所有 `.md` 文件必须使用 UTF-8 编码。

---

# 第三部分：待办事项（内容缺口）

以下为已知待办内容，完成前不阻塞现有发布流程：

1. **《工具清单》附录**：结构建造章「三、用品简介」承诺将不常用工具整理为附录，目前未写（需结构组提供清单，完成后同步六语言）
2. **激光切割工艺参数附录**：同章「激光切割耗材」注明功率、速度等工艺参数放附录持续更新，目前未写（需实验室实测数据）
3. **开源许可**：版权页（封二）预留的许可位置留空待定，正式发布前建议明确许可（如 CC BY-NC-SA 4.0 或团队内部限定）
