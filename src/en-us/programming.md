# Programming

## 1. Basic Requirements

The following are supplementary requirements for Programming.

### Applications

- Git
- Visual Studio Code
- Android Studio

---

## 2. Environment Setup

The following environment must be configured before you begin. If you have any questions, please consult an administrator.

### Web Browser

Bookmark the following additional websites:

| Name | URL |
|------|------|
| Programming Resources | https://www.firstinspires.org/resources/library/ftc/programming-resources |
| REV Robotics Documentation | https://docs.revrobotics.com/duo-control/hello-robot-java/welcome |
| Pedro Pathing | https://pedropathing.com/ |
| Robot Dashboard | http://192.168.43.1:8080/ |

### Git

Git is the version control tool adopted by our team for program files. Android Studio does not bundle Git — install and configure it using either method below.

**Method 1 (download and install Git within Android Studio):**

1. Open Android Studio and go to Settings: File → Settings on Windows/Linux; Android Studio → Settings (or Preferences) on macOS
2. Expand Version Control in the left menu and click Git
3. If Git is not detected, the dialog provides a download entry — click it to download and install Git
4. After installation, confirm the Git executable path under Path to Git executable (git.exe on Windows); click Test until it shows Successful, then click Apply and OK

**Method 2 (install Git separately first, then configure the path in Android Studio):**

1. Visit the official Git website at [https://git-scm.com/downloads](https://git-scm.com/downloads) and download the installer for your system (Windows / macOS / Linux)
2. Run the installer and accept the defaults by clicking Next
3. Open Android Studio and go to Settings → Version Control → Git
4. Enter or browse to the Git executable path under Path to Git executable (auto-detected if the PATH environment variable is set)
5. Click Test; once it shows Successful, click Apply and OK

To enable version control for the current project: click VCS in the top menu → Enable Version Control Integration..., choose Git, and click OK.

### Android Studio

Android Studio is the IDE adopted by our team for writing programs.

**Software installation and configuration:**

1. Open [https://developer.android.com/studio](https://developer.android.com/studio)
2. Click "Download Android Studio" and install the version for your platform.

**On Windows, note the following during installation:**

- Both checkboxes must be checked
- Choose a path with sufficient space that will not be moved

**Initialization:**

- Select "Standard" mode
- Check "Accept" when agreeing to the licenses
- Keep everything else unchanged and click "Next"

**Installing the Chinese language pack (optional):**

1. Open the [Android Studio Chinese Language Pack releases](https://github.com/sollyu/AndroidStudioChineseLanguagePack/releases)
2. Download the latest language pack (.jar file)
3. In the left tab list on the welcome screen, select "Plugins", then "Install Plugin from Disk"
4. Select the downloaded .jar file and open it; make sure the plugin is enabled once loaded
5. In the left tab list, select "Customize", open "Language and Region", select "Chinese (Simplified)" under "Language", choose "Americas" under "Region", then restart

**Cloning the repository:**

1. Click "GitHub" in the left tab list and sign in via "Log in with GitHub" to authorize.
2. Select the current season's code repository (e.g., `ftc32477/FTC-32477-Decode-Program`)
3. Choose an empty folder on a path that will not change and click "Clone"
4. Wait for the download to finish; track progress via the "Build" tab in the left sidebar or the progress bar in the bottom-right corner

> [!warning] If you run into problems, ask an administrator.

### Visual Studio Code

Visual Studio Code is the tool adopted by our team for code editing and history viewing.

**Software installation and configuration:**

1. Open [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download)
2. Download and install the build for your platform
3. Install the [Chinese language pack](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans) if you want the UI in Chinese.

---

## 3. Tools Overview

### Android Studio

Official documentation: [https://developer.android.com/studio/intro?hl=en](https://developer.android.com/studio/intro?hl=en)

In this project, we build on the official FTC application framework and write robot control programs in Java under the `TeamCode` folder, calling upon the various dependency libraries needed for robot operation.

For the essentials you need to know about Android Studio, refer to the quick UI walkthrough in the official documentation.

### Visual Studio Code

Official documentation: [https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)

Since Visual Studio Code follows similar operating logic to Android Studio and is used less frequently in this project, refer to the Android Studio section for interface guidance.

### Robot Dashboard

- Connect to the Wi-Fi network "`32477-RC`". Wi-Fi password: ask an administrator or obtain it via the Driver Hub.
- URL: [http://192.168.43.1:8080/](http://192.168.43.1:8080/)
- This is the web page of the Wi-Fi module built into the Control Hub (officially called the Robot Controller Console), providing a graphical management console for the Control Hub.

For the essentials you need to know about the Robot Dashboard, refer to the quick UI walkthrough in the official documentation.

---

## 4. Workflow

The Programming team's core work consists of three parts:

- **Autonomous programs**: control logic for the season's Autonomous period
- **TeleOp programs**: operation logic for the driver-controlled period
- **Sensor configuration**: configuration of sensors and vision systems

### Debugging Is the Core

> [!info] The real difficulty in program development lies in debugging. Autonomous paths, driver controls, PID parameters, vision configuration — most sensors come with ready-made packages you can reuse. What you really do is *tune*.

Debugging runs through the entire development workflow:

1. **Requirements analysis**: clarify the rules and task requirements of the current season
2. **Architecture design**: design the overall program architecture and module breakdown
3. **Implementation**: write Java code in Android Studio
4. **Version control**: manage code versions with Git
5. **Debugging**: tune autonomous paths, driver controls, PID parameters, and vision configuration
6. **Testing & verification**: verify program functionality on the robot
7. **Code review**: review and merge code via GitHub
8. **Deployment**: deploy the final build to the Robot Controller
