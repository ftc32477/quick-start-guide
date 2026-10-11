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
2. Select the program repository for the current season (one is created for each season; names follow the pattern `FTC-32477-<season>-Program`; confirm with an administrator before the new season's repository is created)
3. Choose an empty folder on a path that will not change and click "Clone"
4. Wait for the download to finish; track progress via the "Build" tab in the left sidebar or the progress bar in the bottom-right corner

> [!warning] If you run into problems, ask an administrator.

### Visual Studio Code

Visual Studio Code is the tool adopted by our team for code editing and history viewing.

**Software installation and configuration:**

1. Open [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download)
2. Download and install the build for your platform
3. Install the [VS Code Chinese language pack](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans) if you want the UI in Chinese.

---

## 3. Tools Overview

### Android Studio

Official documentation: [https://developer.android.com/studio/intro?hl=en](https://developer.android.com/studio/intro?hl=en)

This project builds on the official FTC application framework: robot control programs are written in Java under the `TeamCode` folder, calling the dependency libraries needed for operation.

For the essentials you need to know about Android Studio, refer to the quick UI walkthrough in the official documentation.

### Visual Studio Code

Official documentation: [https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)

Visual Studio Code follows the same operating logic as Android Studio and is used less frequently; for interface operations, refer to the Android Studio section.

### Robot Dashboard

- Connect to the Wi-Fi network "`32477-RC`". Wi-Fi password: ask an administrator or obtain it via the Driver Hub.
- URL: [http://192.168.43.1:8080/](http://192.168.43.1:8080/) (accessible only within the robot's local network)
- This is the web page of the Wi-Fi module built into the Control Hub (officially called the Robot Controller Console), providing a graphical management console for the Control Hub.

For the essentials you need to know about the Robot Dashboard, refer to the quick UI walkthrough in the official documentation.

---

## 4. Workflow

The Programming team's core work consists of three parts:

- **Autonomous programs**: control logic for the season's Autonomous period
- **TeleOp programs**: operation logic for the driver-controlled period
- **Sensor configuration**: configuration of sensors and vision systems

> [!info] Driver operation: the competition robot is driven with an Xbox controller; officially only the Xbox 360 model is permitted. Drivers are selected from within the team; familiarity with controller operation is an advantage.

### Debugging Is the Core

> [!info] The difficulty of program development lies mainly in debugging. Autonomous paths, driver controls, PID parameters, vision configuration, and similar areas mostly have ready-made packages that can be reused; the focus of the work is parameter tuning and verification.

Debugging runs through the entire development workflow:

1. **Requirements analysis**: clarify the rules and task requirements of the current season
2. **Architecture design**: design the overall program architecture and module breakdown
3. **Implementation**: write Java code in Android Studio
4. **Version control**: manage code versions with Git
5. **Debugging**: tune autonomous paths, driver controls, PID parameters, and vision configuration
6. **Testing & verification**: verify program functionality on the robot
7. **Code review**: review and merge code via GitHub
8. **Deployment**: deploy the final build to the Robot Controller


### AI-Assisted Programming

> [!info] AI Agent and similar tools can assist program development. The core skill is being able to **read AI-generated code, determine what to change, and know how to debug**; you do not need to write all the code from scratch.

- Core programming logic (e.g., for loops, while loops) is universal across languages; only the syntax differs. Students with C++ experience can adapt to Java quickly

---

## 5. GitHub Collaboration Basics

> [!info] This section covers the minimum you need to use GitHub: viewing repositories, downloading files, submitting feedback, making changes, collaborating, and finding open-source projects. See the official documentation links at the end of this section for complete details. Interface buttons are in English; labels are given as they appear on screen.

### What GitHub Is

GitHub is a **code hosting and collaboration platform** built on Git: code is stored in the cloud (repositories) with a complete edit history (commits), multiple people can collaborate on the same project (branches, pull requests), and it provides companion tools such as issues, automation (Actions), and website hosting (Pages).

The team's main uses of GitHub:

- **Storing season programs**: one public repository is created for each season (forked from the official SDK template) and archived as read-only after the season ends; once the new season's repository is created, it will be added to the table in this section.
- **Maintaining the Quick Start Guide**: the source files and build scripts are stored in the public repository `ftc32477/quick-start-guide`.
- **Publishing the team site**: the site publishing repository is `ftc32477/ftc32477.github.io`; each section is built from its own source repository by GitHub Actions and pushed to its corresponding subpath (this guide → `/docs/`); the root path currently redirects to `/docs/`. Future resources will each get their own source repository and be pushed to their own subpath.
- **Finding open-source projects**: search for general engineering tools and for code and solutions shared by the FTC community.

**Accounts and the organization**: use your own account (for registration, see Team Member Essentials), and wait for an administrator to invite you to join the `ftc32477` organization. Repositories belong to the organization, and permissions are assigned by administrators according to role:

| Role | What you can do (summary) |
|------|---------------------------|
| Read | View and discuss projects |
| Triage | Manage issues and pull requests, but cannot write code |
| Write | Push content to repositories |
| Maintain | Manage repositories, but cannot perform sensitive or destructive actions |
| Admin | Full access, including operations such as deleting repositories |

> [!warning] Without write access, submit changes through a pull request or hand them to a maintainer; if you cannot determine your permissions, operate as read-only — do not probe or bypass permission restrictions.

### Terminology Quick Reference

| Term | Meaning (one sentence) |
|------|------------------------|
| Repository | The storage location for a project's files and complete history |
| Commit | A snapshot of changes with a message; commits form the history |
| Branch | A parallel line of development within a repository; changes land on a branch first |
| Clone | A full download of a repository to your local computer |
| Fork | A copy of someone else's repository under your own account; changes do not affect the original |
| Pull request (PR) | The mechanism for requesting review and merging of a branch's changes; the core of collaboration |
| Issue | A discussion thread for questions, bug reports, and suggestions |
| Release | A numbered official release with downloadable files (such as the guide PDF) |
| Star | A bookmark and a like; also used to gauge a project's popularity |
| Watch | A subscription to notifications about a repository's activity |
| Actions | GitHub's automation pipelines (used in this project to build and publish the site) |
| Pages | GitHub's static website hosting (this project's site is published through it) |
| README | The documentation on the repository home page; read it first |

### Team Repository Map

| Repository | Description | How to modify |
|------------|-------------|---------------|
| `quick-start-guide` | Guide source files, build scripts, and site output (public) | Submit a pull request, or hand changes to a maintainer |
| `ftc32477.github.io` | Team site publishing repository (public); content is pushed automatically from the source repositories | Do not modify directly |
| `.github` | Organization profile materials, such as the organization bio (public) | Submit a pull request, or hand changes to a maintainer |
| `FTC-32477-<season>-Program` | Season program repository (public): created separately each season, with old seasons archived as read-only; the specific name will be added once the new season's repository is created | Per the Programming team's internal division of labor |

> [!danger] **Do not touch the publishing repository**: all content in `ftc32477.github.io` comes from its respective source repositories and is pushed automatically by GitHub Actions; direct edits are overwritten by the next push. Do not click edit, commit, or delete in that repository or on any generated content. Site issues must always be handled in the corresponding source repository (`quick-start-guide` for this guide).

### Browsing and Downloading

1. Open the organization home page at [https://github.com/ftc32477](https://github.com/ftc32477) and enter a repository from the Repositories list
2. Read the repository's **README** first (project purpose, usage); the About section on the right has a description and a website link
3. Top tabs (visibility depends on your permissions):
   - **Code**: file list and commit history
   - **Issues**: problems and suggestions
   - **Pull requests**: changes awaiting review
   - **Actions**: automated build and publish records
   - **Releases**: official versions and downloadable files
4. Download the entire repository: Code → **Download ZIP**
5. Download the guide PDF: open **Releases**, select a version, and download the build for your language under Assets
6. View history: the **Commits** list on the Code page → open an individual commit to see the specific changes (diff)

### Reporting Problems (Issues)

Use an issue to report a failure, a documentation error, or a suggestion:

1. Open the target repository's **Issues** tab and search first for an existing report of the same problem
2. Click **New issue** and state the problem in a one-line title
3. In the body, write clearly: **what happened**, **the expected result**, **how to reproduce it** (steps), and relevant screenshots (remove personal information first)
4. After submitting, watch for replies; once the problem is resolved, a maintainer closes the issue

> [!info] The guide's permanent feedback entry point: [https://github.com/ftc32477/quick-start-guide/issues](https://github.com/ftc32477/quick-start-guide/issues)

### Editing in the Browser (Edit → Open a PR)

Without write access, GitHub automatically turns browser-based changes into a "fork + pull request (PR)" workflow:

1. Sign in and open the file you want to change (for example, a `.md` file under the guide's `src/en-us/`)
2. Click the pencil icon **Edit this file** in the top-right corner of the file
3. If you do not have write access, the page will prompt you that a fork will be created automatically; accept the prompt
4. Make your changes and enter a clear one-line description in **Commit changes**
5. Select **Create a new branch for this commit and start a pull request**, with a branch name such as `fix/typo-member`
6. In the pull request form that opens, explain what you changed and why, then click **Create pull request**
7. Wait for a maintainer to review; if there are comments, continue revising accordingly; once merged, the changes take effect

> [!warning] Keep one pull request to one change; do not modify files you are unfamiliar with (build scripts, generated output, etc.); never commit anything to the publishing repository.

### Local Collaboration

Working from a local clone is the most common approach. Prerequisite: Git is installed on your computer (see Section 2, Environment Setup). Common commands:

```bash
# Clone the repository to your local computer
git clone https://github.com/ftc32477/quick-start-guide.git
cd quick-start-guide

# Pull the latest changes before starting work
git pull

# Create a new branch for this task
git switch -c feat/my-feature

# After modifying files: check status, stage, commit
git status
git add <file>
git commit -m "Description of this change"

# Push the branch to GitHub
git push -u origin feat/my-feature
```

After pushing, create a pull request for the branch on GitHub and wait for review and merge. Android Studio and Visual Studio Code provide equivalent graphical operations (see Section 2, Environment Setup); the same steps can be completed through their interfaces.

> [!warning] Three rules: **pull before you start**; **one commit does one thing, with a clear message**; **push to your own branch — do not push directly to main**.

**Syncing a fork with upstream (when contributing to external projects)**: a fork does not update automatically. First add the original repository as upstream: `git remote add upstream <original repository URL>`, then sync using `git fetch upstream` and a merge operation (see the "Syncing a fork" section of the official documentation).

### Open-Source Community (Search, Evaluation, and Contribution)

**Searching** (the search box supports qualifiers, which can be combined):

- `topic:ftc`, `topic:first-tech-challenge`, `topic:ftc-robot`: the main entry points for FTC community projects
- `ftc language:Java sort:updated`: Java projects that are still actively maintained
- `"FIRST Tech Challenge" in:readme`: projects whose README mentions FTC

Common FTC open-source resources (all available on GitHub):

| Project | Purpose |
|---------|---------|
| FIRST-Tech-Challenge/FtcRobotController | Official FTC SDK and examples |
| FTCLib/FTCLib | Common FTC utility library |
| acmerobotics/road-runner | Motion planning and path following |
| Pedro-Pathing/PedroPathing | Path planning |
| acmerobotics/ftc-dashboard | Debugging dashboard |
| OpenFTC/EasyOpenCV | Vision processing |
| the-orange-alliance, ftc-scout/ftc-scout | Event data and statistics |

**Evaluating whether a repository is usable (five checks)**: date of the latest commit (whether it is still maintained), README and documentation quality, license, issue activity, and whether official releases exist.

**License quick reference** (essential reading before using someone else's code or assets):

| License | One-sentence summary |
|---------|---------------------|
| MIT | Most permissive: free to use as long as you keep the copyright notice |
| Apache-2.0 | Also permissive, with additional patent grant and change notice requirements |
| GPL-3.0 | Copyleft: derivative works based on it must also be open-sourced |
| No license | Defaults to "all rights reserved"; you **cannot** copy or use it directly and must contact the author first |

**Contributing**: read the project's `CONTRIBUTING.md` (contribution guidelines) and code of conduct in the root directory first; discuss uncertain changes in an issue first; submit small fixes through the "Edit → Open a PR" process above.

> [!warning] Security: do not run scripts or executables from unknown sources; do not post API keys, passwords, or tokens in issues or repositories; be wary of installation commands such as `curl | bash`.

### Dangerous Operations Warning

> [!danger] The following operations can cause irreversible loss and must not be performed by regular team members; if an operation is truly necessary, confirm with an administrator first.

- Editing the publishing repository `ftc32477.github.io` directly (the change is overwritten and pollutes the production site)
- `git push --force`: forcibly overwrites remote history and may make teammates' commits disappear
- `git reset --hard`: discards unpushed local changes, which are difficult to recover
- Deleting branches or repositories, or changing a repository's visibility, name, or ownership
- Committing keys, passwords, or tokens to a repository (once public, they remain in the history even after deletion; revoke and replace them immediately)
- Posting internal materials or private information (email addresses, home addresses, personal information in screenshots) in issues, pull requests, or public repositories
- Running or merging code from unknown sources

> [!info] Account security: do not share your account with others; GitHub is enforcing two-factor authentication (2FA) for accounts that contribute code — enable it when prompted; create personal access tokens with the minimum permissions required and never write them into code or repositories.

### Practice Checklist

1. Open the organization home page, enter the `quick-start-guide` repository, and use the README to explain what the project does
2. Download the guide PDF in any language from Releases
3. Find the most recent change in the commit history and explain what it changed
4. Search Issues for "PDF" and check whether there are related reports
5. Fix a typo using the "Edit → Open a PR" process and submit a pull request

### Official Documentation Links

For more advanced usage, consult the following official documentation as needed:

- GitHub quickstart: [https://docs.github.com/en/get-started/quickstart](https://docs.github.com/en/get-started/quickstart)
- Writing and storing your code (branches/commits/PRs): [https://docs.github.com/en/get-started/start-your-journey/writing-and-storing-your-code](https://docs.github.com/en/get-started/start-your-journey/writing-and-storing-your-code)
- Git cheatsheet: [https://docs.github.com/en/get-started/git-basics/git-cheatsheet](https://docs.github.com/en/get-started/git-basics/git-cheatsheet)
- Search syntax: [https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax)
- Repository roles for an organization: [https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization)
- Interactive course (English): [https://skills.github.com/](https://skills.github.com/)

> [!info] When unsure about an operation, ask an administrator or raise the question in an issue first.
