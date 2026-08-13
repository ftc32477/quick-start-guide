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

**汉化：**

1. 打开 [Android Studio 中文语言包](https://github.com/sollyu/AndroidStudioChineseLanguagePack/releases)
2. 下载最新的语言扩展包（.jar 文件）
3. 在主页面的左侧选项卡列表中选择"Plugins"，选择"Install Plugin from Disk"
4. 选择下载的 .jar 文件并打开，插件加载成功后确保其处于开启状态
5. 在左侧选项卡列表中选择"Customize"，进入"语言和地区（Language and Region）"，将"语言（Language）"选择为"Chinese (Simplified) 简体中文"，将"地区（Region）"选择为"Americas"，然后重启

**克隆仓库：**

1. 点击左侧选项卡列表中的"GitHub"，点击"通过 GitHub 登录"进行授权。
2. 选择当前赛季的代码仓库（如：`ftc32477/FTC-32477-Decode-Program`）
3. 选择一个不会改变路径的空文件夹，点击"克隆"
4. 等待文件下载完成，在左侧边栏的"构建"选项卡或窗口右下通过进度条查看进度

> [!warning] 如有问题，请向管理员咨询。

### Visual Studio Code

Visual Studio Code 是我队采用的代码编辑与历史查看工具。

**软件安装及环境配置流程：**

1. 打开 [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download)
2. 下载对应版本并安装即可
3. 打开 [汉化插件](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans)，安装该插件即可汉化。

---

## 三、用品简介

### Android Studio

官方文档：[https://developer.android.com/studio/intro?hl=zh-cn](https://developer.android.com/studio/intro?hl=zh-cn)

在本项目中，我们基于 FTC 官方提供的应用框架，在 `TeamCode` 文件夹下使用 Java 语言编写机器人控制程序，以调用机器人运行所需的各类依赖库。

关于 Android Studio 所需掌握的基本知识，请参考官方文档中的简易页面指引。

### Visual Studio Code

官方文档：[https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)

鉴于 Visual Studio Code 与 Android Studio 操作逻辑类似，且前者在本项目中使用频次较低，相关界面指引请参考 Android Studio 部分，此处不再赘述。

### Robot Dashboard

- 连接 Wi-Fi 网络"`32477-RC`"。Wi-Fi 密码：询问管理员或通过 Driver Hub 获取。
- 网址是：[http://192.168.43.1:8080/](http://192.168.43.1:8080/)
- 这是 Control Hub 内置的 Wi-Fi 模块的 Web 页面（官方名称为 Robot Controller Console，即机器人控制器控制台），提供了管理 Control Hub 的图形化后台。

关于 Robot Dashboard 所需掌握的基本知识，请参考官方文档中的简易页面指引。

---

## 四、工作流程

程序设计组的核心工作分为三部分：

- **自动程序**：赛季自动阶段（Auto）的控制逻辑
- **手动程序**：遥控阶段（TeleOp）的操作逻辑
- **传感器配置**：各类传感器、视觉系统的配置

### 调试是核心

> [!info] 程序开发的真正难点在于调试。自动路径、手动操作、PID 参数、视觉配置——大部分传感器都有现成的程序包可以直接复用，你真正要做的是"调"。

调试工作贯穿整个开发流程：

1. **需求分析**：明确当前赛季的规则和任务需求
2. **架构设计**：设计程序整体架构和模块划分
3. **代码编写**：在 Android Studio 中编写 Java 代码
4. **版本控制**：使用 Git 进行代码版本管理
5. **调试**：调自动路径、调手动操作、调 PID 参数、调视觉配置
6. **测试验证**：在机器人上验证程序功能
7. **代码审查**：通过 GitHub 进行代码审查和合并
8. **部署发布**：将最终版本部署到 Robot Controller
