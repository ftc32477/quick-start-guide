# 程序设计

## 一、基本资料

以下是程序设计需要追加的资料。

### 应用程序

- Git
- Visual Studio Code
- Android Studio

---

## 二、环境配置

以下是在正式开始前需要配置的工作环境，请按照说明操作。如有疑问，请向管理员咨询。

### 网络浏览器

需要追加收藏保存的网址如下：

| 名称 | 地址 |
|------|------|
| Programming Resources | https://www.firstinspires.org/resources/library/ftc/programming-resources |
| REV Robotics Documentation | https://docs.revrobotics.com/duo-control/hello-robot-java/welcome |
| Pedro Pathing | https://pedropathing.com/ |
| Robot Dashboard | http://192.168.43.1:8080/ |

### Git

Git 是我队采用的程序文件版本控制工具。Android Studio 不自带 Git，需要安装并配置，以下两种方式任选其一。

**方式一（在 Android Studio 中下载并安装 Git）：**

1. 打开 Android Studio，进入设置页面：Windows/Linux 为 File → Settings，macOS 为 Android Studio → Settings（或 Preferences）
2. 在左侧菜单展开 Version Control，点击 Git
3. 若未检测到 Git，界面会提供下载入口，点击下载并安装即可
4. 安装完成后，在 Path to Git executable 中确认 Git 程序路径（Windows 为 git.exe），点击 Test 显示 Successful 后，点击 Apply 与 OK 保存

**方式二（先单独安装 Git，再在 Android Studio 中配置路径）：**

1. 访问 Git 官网 [https://git-scm.com/downloads](https://git-scm.com/downloads)，下载适合你电脑系统（Windows / macOS / Linux）的安装包
2. 运行安装程序，按默认选项一路 Next 完成安装
3. 打开 Android Studio，进入设置 → Version Control → Git
4. 在 Path to Git executable 中输入或选择 Git 程序路径（已配置环境变量时会自动识别）
5. 点击 Test，显示 Successful 后点击 Apply 与 OK 保存

如需要在当前项目启用版本控制：点击顶部菜单 VCS → Enable Version Control Integration...，选择 Git 并点击 OK。

### Android Studio

Android Studio 是我队采用的程序编写工具。

**软件安装及环境配置流程：**

1. 打开 [https://developer.android.com/studio](https://developer.android.com/studio)
2. 点击"Download Android Studio"，下载对应版本并安装。

**在 Windows 中安装时需要注意：**

- 两个复选框均须勾选
- 选择一个空间充足且不会被改变的路径地址

**初始化：**

- 请选择"Standard"模式
- 同意协议时请勾选"Accept"
- 其他请保持不变并选择"Next"

**安装中文语言包（可选）：**

1. 打开 [Android Studio 中文语言包](https://github.com/sollyu/AndroidStudioChineseLanguagePack/releases)
2. 下载最新的语言扩展包（.jar 文件）
3. 在主页面的左侧选项卡列表中选择"Plugins"，选择"Install Plugin from Disk"
4. 选择下载的 .jar 文件并打开，插件加载成功后确保其处于开启状态
5. 在左侧选项卡列表中选择"Customize"，进入"语言和地区（Language and Region）"，将"语言（Language）"选择为"Chinese (Simplified) 简体中文"，将"地区（Region）"选择为"Americas"，然后重启

**克隆仓库：**

1. 点击左侧选项卡列表中的"GitHub"，点击"通过 GitHub 登录"进行授权。
2. 选择当前赛季对应的程序仓库（每赛季单独建立，名称形如 `FTC-32477-<赛季>-Program`；新赛季仓库建立前先向管理员确认）
3. 选择一个不会改变路径的空文件夹，点击"克隆"
4. 等待文件下载完成，在左侧边栏的"构建（Build）"选项卡或窗口右下通过进度条查看进度

> [!warning] 如有问题，请向管理员咨询。

### Visual Studio Code

Visual Studio Code 是我队采用的代码编辑与历史查看工具。

**软件安装及环境配置流程：**

1. 打开 [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download)
2. 下载对应版本并安装即可
3. 如需中文界面，安装 [VS Code 中文语言包](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans)。

---

## 三、用品简介

### Android Studio

官方文档：[https://developer.android.com/studio/intro?hl=zh-cn](https://developer.android.com/studio/intro?hl=zh-cn)

本项目基于 FTC 官方应用框架，在 `TeamCode` 文件夹中使用 Java 编写机器人控制程序，并调用运行所需的依赖库。

关于 Android Studio 所需掌握的基本知识，请参考官方文档中的简易页面指引。

### Visual Studio Code

官方文档：[https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)

Visual Studio Code 与 Android Studio 的操作逻辑类似，且使用频次较低；界面操作请参考 Android Studio 部分。

### Robot Dashboard

- 连接 Wi-Fi 网络"`32477-RC`"。Wi-Fi 密码：询问管理员或通过 Driver Hub 获取。
- 网址是：[http://192.168.43.1:8080/](http://192.168.43.1:8080/)（仅在机器人局域网内可访问）
- 这是 Control Hub 内置的 Wi-Fi 模块的 Web 页面（官方名称为 Robot Controller Console，即机器人控制器控制台），提供了管理 Control Hub 的图形化后台。

关于 Robot Dashboard 所需掌握的基本知识，请参考官方文档中的简易页面指引。

---

## 四、工作流程

程序设计组的核心工作分为三部分：

- **自动程序**：赛季自动阶段（Auto）的控制逻辑
- **手动程序**：遥控阶段（TeleOp）的操作逻辑
- **传感器配置**：各类传感器、视觉系统的配置

> [!info] 手柄操作（Driver）：参赛机器人使用 Xbox 手柄操控，官方仅允许 Xbox 360 型号；Driver 由队内选拔产生，熟悉手柄操作者更具优势。

### 调试是核心

> [!info] 程序开发的难点主要在调试。自动路径、手动操作、PID 参数、视觉配置等，多数已有现成程序包可复用，工作重点是参数调整与验证。

调试工作贯穿整个开发流程：

1. **需求分析**：明确当前赛季的规则和任务需求
2. **架构设计**：设计程序整体架构和模块划分
3. **代码编写**：在 Android Studio 中编写 Java 代码
4. **版本控制**：使用 Git 进行代码版本管理
5. **调试**：调自动路径、调手动操作、调 PID 参数、调视觉配置
6. **测试验证**：在机器人上验证程序功能
7. **代码审查**：通过 GitHub 进行代码审查和合并
8. **部署发布**：将最终版本部署到 Robot Controller

### AI 辅助编程

> [!info] 程序开发可使用 AI Agent 等工具辅助。核心能力是**读懂 AI 生成的代码、明确修改方向并掌握调试方法**，不必从零手写全部代码。

- 各类编程语言的核心逻辑（如 for 循环、while 循环）是通用的，仅语法存在差异；有 C++ 基础的同学可以快速适应 Java 开发

---

## 五、GitHub 协作基础

> [!info] 本节覆盖使用 GitHub 所需的最小内容：查看仓库、下载文件、提交反馈、修改内容、参与协作与查找开源项目。完整说明见文末的官方文档入口。界面按钮以英文为主，文中以"英文（中文）"形式标注。

### GitHub 是什么

GitHub 是基于 Git 的**代码托管与协作平台**：代码存在云端（仓库）并保留完整修改历史（提交），多人可以在同一项目上协作（分支、拉取请求），还配套了议题、自动化（Actions）、网站托管（Pages）等工具。

本队使用 GitHub 的主要用途：

- **存放赛季程序**：每个赛季单独建立一个公开仓库（从官方 SDK 模板复刻），赛季结束后归档为只读；新赛季仓库建立后补入本节表格。
- **维护《快速入门指南》**：源文件与构建脚本存放在公开仓库 `ftc32477/quick-start-guide`。
- **发布团队站点**：站点发布仓库为 `ftc32477/ftc32477.github.io`，各栏目由各自的源仓库经 GitHub Actions 构建后推送到对应子路径（本指南 → `/docs/`）；根路径当前重定向到 `/docs/`。后续各类资源将分别建立源仓库并推送到各自子路径。
- **查找开源项目**：检索通用工程工具，以及 FTC 社区共享的代码与方案。

**账号与组织**：使用本人账号（注册流程见《队员须知》），由管理员邀请加入组织 `ftc32477`。仓库归组织所有，操作权限由管理员按角色分配：

| 角色 | 能做的事（摘要） |
|------|------|
| 读取（Read） | 查看与讨论项目 |
| 分类（Triage） | 管理议题与拉取请求，但不能写入代码 |
| 写入（Write） | 向仓库推送内容 |
| 维护（Maintain） | 管理仓库，但不能做敏感或破坏性操作 |
| 管理（Admin） | 完全权限，含删除仓库等操作 |

> [!warning] 没有写入权限时，改动通过拉取请求提交或交由维护者处理；无法确定权限时按只读方式操作，不要探测或绕过权限限制。

### 名词速查

| 名词 | 含义（一句话） |
|------|----------------|
| 仓库（Repository） | 项目文件与完整历史记录的存储位置 |
| 提交（Commit） | 一次带说明的修改快照，构成历史记录 |
| 分支（Branch） | 仓库内的并行开发线，改动先落在分支上 |
| 克隆（Clone） | 把仓库完整下载到本地电脑 |
| 复刻（Fork） | 把别人的仓库复制一份到自己账号下，改动不影响原仓库 |
| 拉取请求（Pull Request，PR） | 请求审查并合并某分支改动的机制，协作的核心 |
| 议题（Issue） | 提问、报错、建议的讨论帖 |
| 发行版（Release） | 打上版本号的正式发布，附可下载文件（如指南 PDF） |
| 星标（Star） | 收藏与点赞，也用于判断项目人气 |
| 关注（Watch） | 订阅仓库动态通知 |
| Actions | GitHub 的自动化流水线（本项目用于构建与发布站点） |
| Pages | GitHub 的静态网站托管（本项目站点即由此发布） |
| README | 仓库首页的说明文档，应首先阅读 |

### 团队仓库地图

| 仓库 | 说明 | 修改方式 |
|------|------|----------|
| `quick-start-guide` | 指南源文件、构建脚本与站点产物（公开） | 提交拉取请求，或交由维护者处理 |
| `ftc32477.github.io` | 团队站点发布仓库（公开），内容由各源仓库自动推送 | 不直接修改 |
| `.github` | 组织主页资料，如组织简介（公开） | 提交拉取请求，或交由维护者处理 |
| `FTC-32477-<赛季>-Program` | 赛季程序仓库（公开）：每赛季单独建立，旧赛季归档为只读；新赛季仓库建立后补充具体名称 | 按程序组内部分工 |

> [!danger] **发布仓库禁区**：`ftc32477.github.io` 的所有内容均来自各自的源仓库，由 GitHub Actions 自动推送；直接修改会在下一次推送时被覆盖。不要在该仓库或任何生成内容上点击编辑、提交或删除。站点问题一律回到对应源仓库处理（本指南为 `quick-start-guide`）。

### 浏览与下载

1. 打开组织主页 [https://github.com/ftc32477](https://github.com/ftc32477)，在 Repositories 列表中进入仓库
2. 先读仓库首页的 **README**（项目用途、使用方法）；右侧 About 区有简介与主页链接
3. 顶部页签（是否可见取决于权限）：
   - **Code**：文件列表与提交历史
   - **Issues**：问题与建议
   - **Pull requests**：待审查的改动
   - **Actions**：自动化构建与发布记录
   - **Releases**：正式版本与下载文件
4. 下载整个仓库：Code → **Download ZIP**
5. 下载指南 PDF：进入 **Releases**，选择版本，在 Assets 中下载对应语言
6. 查看历史：Code 页的 **Commits** 列表 → 点进单次提交查看具体改动（diff）

### 反馈问题（Issue）

遇到故障、文档错误或有建议时，用 Issue 反馈：

1. 打开目标仓库的 **Issues** 页签，先搜索是否已有相同问题
2. 点击 **New issue**，用一句话标题说明问题
3. 正文写清：**发生了什么**、**期望的结果**、**如何复现**（步骤）、相关截图（先去掉个人信息）
4. 提交后关注回复；问题解决后由维护者关闭

> [!info] 指南的固定反馈入口：[https://github.com/ftc32477/quick-start-guide/issues](https://github.com/ftc32477/quick-start-guide/issues)

### 网页端修改（编辑 → 提 PR）

没有写入权限时，GitHub 会自动把网页端改动做成"复刻（Fork）+ 拉取请求（PR）"：

1. 登录后打开要修改的文件（如指南 `src/zh-hans/` 下的某篇 `.md`）
2. 点击文件右上角的铅笔图标 **Edit this file**
3. 若无写入权限，页面会提示将自动创建复刻，同意即可
4. 修改内容，在 **Commit changes** 中填写一句清晰的说明
5. 选择 **Create a new branch for this commit and start a pull request**，分支名如 `fix/typo-member`
6. 在打开的 PR 表单中说明修改内容与原因，点击 **Create pull request**
7. 等待维护者审查；如有评论，按意见继续修改，合并后改动即生效

> [!warning] 一次 PR 只提交一件事；不要修改不熟悉的文件（构建脚本、生成产物等）；发布仓库不提交任何改动。

### 本地协作

在本地克隆仓库开发是最常用的方式。前提是本机已安装 Git（见"二、环境配置"）。常用命令如下：

```bash
# 克隆仓库到本地
git clone https://github.com/ftc32477/quick-start-guide.git
cd quick-start-guide

# 开始工作前先拉取最新改动
git pull

# 为本次工作新建分支
git switch -c feat/my-feature

# 修改文件后：查看状态、暂存、提交
git status
git add <文件>
git commit -m "本次修改说明"

# 推送分支到 GitHub
git push -u origin feat/my-feature
```

推送后，在 GitHub 上为该分支创建 Pull Request，等待审查合并。Android Studio 与 Visual Studio Code 提供等效的图形操作（见"二、环境配置"），可用界面完成同样步骤。

> [!warning] 三条纪律：**先 pull 再动手**；**一次提交只做一件事、说明写清楚**；**推送到自己的分支，不直接推 main**。

**复刻与上游同步（参与外部项目时）**：复刻的仓库不会自动更新。需要先添加原仓库为上游：`git remote add upstream <原仓库地址>`，再用 `git fetch upstream` 与合并操作同步（详见官方文档"同步复刻"一节）。

### 开源社区（检索、评估与贡献）

**检索**（搜索框支持限定词，可组合使用）：

- `topic:ftc`、`topic:first-tech-challenge`、`topic:ftc-robot`：FTC 社区项目的总入口
- `ftc language:Java sort:updated`：最近仍在维护的 Java 项目
- `"FIRST Tech Challenge" in:readme`：README 中提及 FTC 的项目

FTC 常用开源资源（均可在 GitHub 找到）：

| 项目 | 用途 |
|------|------|
| FIRST-Tech-Challenge/FtcRobotController | FTC 官方 SDK 与示例 |
| FTCLib/FTCLib | FTC 常用工具库 |
| acmerobotics/road-runner | 动作规划与路径跟随 |
| Pedro-Pathing/PedroPathing | 路径规划 |
| acmerobotics/ftc-dashboard | 调试仪表盘 |
| OpenFTC/EasyOpenCV | 视觉处理 |
| the-orange-alliance、ftc-scout/ftc-scout | 赛事数据与统计 |

**评估一个仓库是否可用（五看）**：最近提交时间（是否仍在维护）、README 与文档质量、许可证（License）、Issues 活跃度、Releases 有无正式版本。

**许可证速览**（使用别人的代码或素材前必看）：

| 许可证 | 一句话说明 |
|--------|------------|
| MIT | 最宽松：保留版权声明即可自由使用 |
| Apache-2.0 | 同样宽松，另有专利授权与变更声明要求 |
| GPL-3.0 | 具有传染性：基于它的衍生作品也须开源 |
| 无许可证 | 默认"保留所有权利"，**不能**直接复制使用，需先联系作者 |

**参与贡献**：先阅读项目根目录的 `CONTRIBUTING.md`（贡献指南）与行为准则；不确定的改动先开 Issue 讨论；小修小补按上文"编辑 → 提 PR"流程提交。

> [!warning] 安全：不要运行来源不明的脚本或可执行文件；不要把 API Key、密码、Token 发到 Issue 或仓库中；对 `curl | bash` 一类的安装命令保持警惕。

### 危险操作警示

> [!danger] 以下操作可能造成不可逆损失，普通队员一律不要执行；确需操作时先经过管理员确认。

- 直接修改发布仓库 `ftc32477.github.io`（会被覆盖并污染正式站）
- `git push --force`：强制覆盖远端历史，可能让队友的提交消失
- `git reset --hard`：丢弃本机未推送的改动，且难以找回
- 删除分支、删除仓库，或修改仓库的可见性、名称、归属
- 向仓库提交密钥、密码、Token（一旦公开，删除后仍留在历史里，必须立即吊销并重建）
- 在 Issue、PR 或公开仓库中发布内部资料与私人信息（邮箱、住址、截图中的个人信息）
- 运行或合并来源不明的代码

> [!info] 账号安全：不要与他人共享账号；GitHub 正在对参与代码贡献的账号强制要求启用两步验证（2FA），按提示开启；个人访问令牌（Token）按最小权限创建，且绝不写入代码或仓库。

### 练习清单

1. 打开组织主页，进入 `quick-start-guide` 仓库，用 README 说出这个项目是做什么的
2. 在 Releases 中下载任意一种语言的指南 PDF
3. 在提交历史中找到最近一次修改，说出它改了什么
4. 在 Issues 中搜索"PDF"，看看有没有相关问题
5. 按"编辑 → 提 PR"流程修正一处错别字，并提交一个拉取请求

### 官方文档入口

需要更深入的用法时，按需查阅以下官方文档：

- GitHub 快速入门：[https://docs.github.com/zh/get-started/quickstart](https://docs.github.com/zh/get-started/quickstart)
- 编写与保存代码（分支/提交/PR）：[https://docs.github.com/zh/get-started/start-your-journey/writing-and-storing-your-code](https://docs.github.com/zh/get-started/start-your-journey/writing-and-storing-your-code)
- Git 速查表：[https://docs.github.com/zh/get-started/git-basics/git-cheatsheet](https://docs.github.com/zh/get-started/git-basics/git-cheatsheet)
- 搜索语法：[https://docs.github.com/zh/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax](https://docs.github.com/zh/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax)
- GitHub 组织的仓库角色：[https://docs.github.com/zh/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization](https://docs.github.com/zh/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization)
- 交互式课程（英文）：[https://skills.github.com/](https://skills.github.com/)

> [!info] 遇到不确定的操作，先咨询管理员或在 Issues 中提问。
