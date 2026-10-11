# 程式設計

## 一、基本資料

以下是程式設計需要追加的資料。

### 應用程式

- Git
- Visual Studio Code
- Android Studio

---

## 二、環境配置

以下是在正式開始前需要配置的工作環境，請按照說明操作。如有疑問，請向管理員諮詢。

### 網路瀏覽器

需要追加收藏儲存的網址如下：

| 名稱 | 網址 |
|------|------|
| Programming Resources | https://www.firstinspires.org/resources/library/ftc/programming-resources |
| REV Robotics Documentation | https://docs.revrobotics.com/duo-control/hello-robot-java/welcome |
| Pedro Pathing | https://pedropathing.com/ |
| Robot Dashboard | http://192.168.43.1:8080/ |

### Git

Git 是我隊採用的程式檔案版本控制工具。Android Studio 不附帶 Git，需要安裝並配置，以下兩種方式任選其一。

**方式一（在 Android Studio 中下載並安裝 Git）：**

1. 開啟 Android Studio，進入設定頁面：Windows/Linux 為 File → Settings，macOS 為 Android Studio → Settings（或 Preferences）
2. 在左側選單展開 Version Control，點擊 Git
3. 若未偵測到 Git，介面會提供下載入口，點擊下載並安裝即可
4. 安裝完成後，在 Path to Git executable 中確認 Git 程式路徑（Windows 為 git.exe），點擊 Test 顯示 Successful 後，點擊 Apply 與 OK 儲存

**方式二（先單獨安裝 Git，再在 Android Studio 中配置路徑）：**

1. 訪問 Git 官網 [https://git-scm.com/downloads](https://git-scm.com/downloads)，下載適合你電腦系統（Windows / macOS / Linux）的安裝包
2. 執行安裝程式，按預設選項一路 Next 完成安裝
3. 開啟 Android Studio，進入設定 → Version Control → Git
4. 在 Path to Git executable 中輸入或選擇 Git 程式路徑（已配置環境變數時會自動識別）
5. 點擊 Test，顯示 Successful 後點擊 Apply 與 OK 儲存

如需要在目前專案啟用版本控制：點擊頂部選單 VCS → Enable Version Control Integration...，選擇 Git 並點擊 OK。

### Android Studio

Android Studio 是我隊採用的程式編寫工具。

**軟體安裝及環境配置流程：**

1. 開啟 [https://developer.android.com/studio](https://developer.android.com/studio)
2. 點擊「Download Android Studio」，下載對應版本並安裝。

**在 Windows 中安裝時需要注意：**

- 兩個核取方塊均須勾選
- 選擇一個空間充足且不會被改變的路徑地址

**初始化：**

- 請選擇「Standard」模式
- 同意協議時請勾選「Accept」
- 其他請保持不變並選擇「Next」

**安裝中文語言包（可選）：**

1. 開啟 [Android Studio 中文語言套件](https://github.com/sollyu/AndroidStudioChineseLanguagePack/releases)
2. 下載最新的語言擴充套件（.jar 檔案）
3. 在主頁面的左側頁籤清單中選擇「Plugins」，選擇「Install Plugin from Disk」
4. 選擇下載的 .jar 檔案並開啟，外掛載入成功後確保其處於開啟狀態
5. 在左側頁籤清單中選擇「Customize」，進入「語言和地區（Language and Region）」，將「語言（Language）」選擇為「Chinese (Simplified) 簡體中文」，將「地區（Region）」選擇為「Americas」，然後重新啟動

**複製存放庫：**

1. 點擊左側頁籤清單中的「GitHub」，點擊「透過 GitHub 登入」進行授權。
2. 選擇當前賽季對應的程式存放庫（每賽季單獨建立，名稱形如 `FTC-32477-<賽季>-Program`；新賽季存放庫建立前先向管理員確認）
3. 選擇一個不會改變路徑的空資料夾，點擊「複製」
4. 等待檔案下載完成，在左側邊欄的「建置（Build）」頁籤或視窗右下透過進度條查看進度

> [!warning] 如有問題，請向管理員諮詢。

### Visual Studio Code

Visual Studio Code 是我隊採用的程式碼編輯與歷史檢視工具。

**軟體安裝及環境配置流程：**

1. 開啟 [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download)
2. 下載對應版本並安裝即可
3. 如需中文介面，安裝 [VS Code 中文語言包](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans)。

---

## 三、用品簡介

### Android Studio

官方文件：[https://developer.android.com/studio/intro?hl=zh-cn](https://developer.android.com/studio/intro?hl=zh-cn)

本專案基於 FTC 官方應用框架，在 `TeamCode` 資料夾中使用 Java 編寫機器人控制程式，並呼叫執行所需的依賴庫。

關於 Android Studio 所需掌握的基本知識，請參考官方文件中的簡易頁面指引。

### Visual Studio Code

官方文件：[https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)

Visual Studio Code 與 Android Studio 的操作邏輯類似，且使用頻次較低；介面操作請參考 Android Studio 部分。

### Robot Dashboard

- 連接 Wi-Fi 網路「`32477-RC`」。Wi-Fi 密碼：詢問管理員或透過 Driver Hub 取得。
- 網址是：[http://192.168.43.1:8080/](http://192.168.43.1:8080/)（僅在機器人區域網路內可存取）
- 這是 Control Hub 內建的 Wi-Fi 模組的 Web 頁面（官方名稱為 Robot Controller Console，即機器人控制器控制台），提供了管理 Control Hub 的圖形化後台。

關於 Robot Dashboard 所需掌握的基本知識，請參考官方文件中的簡易頁面指引。

---

## 四、工作流程

程式設計組的核心工作分為三部分：

- **自動程式**：賽季自動階段（Auto）的控制邏輯
- **手動程式**：遙控階段（TeleOp）的操作邏輯
- **感測器配置**：各類感測器、視覺系統的配置

> [!info] 手把操作（Driver）：參賽機器人使用有線手把操控（如 Logitech F310、Xbox 360）；官方要求必須為有線連接，允許型號以當季《競賽手冊》為準；Driver 由隊內選拔產生，熟悉手把操作者更具優勢。

### 除錯是核心

> [!info] 程式開發的難點主要在除錯。自動路徑、手動操作、PID 參數、視覺配置等，多數已有現成程式套件可複用，工作重點是參數調整與驗證。

除錯工作貫穿整個開發流程：

1. **需求分析**：明確當前賽季的規則和任務需求
2. **架構設計**：設計程式整體架構和模組劃分
3. **程式碼編寫**：在 Android Studio 中編寫 Java 程式碼
4. **版本控制**：使用 Git 進行程式碼版本管理
5. **除錯**：調自動路徑、調手動操作、調 PID 參數、調視覺配置
6. **測試驗證**：在機器人上驗證程式功能
7. **程式碼審查**：透過 GitHub 進行程式碼審查和合併
8. **部署發布**：將最終版本部署到 Robot Controller

### AI 輔助程式設計

> [!info] 程式開發可使用 AI Agent 等工具輔助。核心能力是**讀懂 AI 生成的程式碼、明確修改方向並掌握除錯方法**，不必從零手寫全部程式碼。

- 各類程式語言的核心邏輯（如 for 迴圈、while 迴圈）是通用的，僅語法存在差異；有 C++ 基礎的同學可以快速適應 Java 開發

---

## 五、GitHub 協作基礎

> [!info] 本節涵蓋使用 GitHub 所需的最小內容：檢視存放庫、下載檔案、提交回饋、修改內容、參與協作與尋找開源專案。完整說明見文末的官方文件入口。介面按鈕以英文為主，文中以「英文（中文）」形式標註。

### GitHub 是什麼

GitHub 是基於 Git 的**程式碼代管與協作平台**：程式碼存在雲端（存放庫）並保留完整的修改歷史（提交），多人可以在同一個專案上協作（分支、提取要求），還配套了問題、自動化（Actions）、網站代管（Pages）等工具。

本隊使用 GitHub 的主要用途：

- **存放賽季程式**：每個賽季單獨建立一個公開存放庫（從官方 SDK 範本分叉），賽季結束後封存為唯讀；新賽季存放庫建立後補入本節表格。
- **維護《快速入門指南》**：原始檔與建置腳本存放在公開存放庫 `ftc32477/quick-start-guide`。
- **發布團隊網站**：網站發布存放庫為 `ftc32477/ftc32477.github.io`，各欄目由各自的來源存放庫經 GitHub Actions 建置後推送到對應子路徑（本指南 → `/docs/`）；根路徑目前重新導向至 `/docs/`。後續各類資源將分別建立來源存放庫並推送到各自子路徑。
- **尋找開源專案**：搜尋通用工程工具，以及 FTC 社群共享的程式碼與方案。

**帳號與組織**：使用本人帳號（註冊流程見《隊員須知》），由管理員邀請加入組織 `ftc32477`。存放庫歸組織所有，操作權限由管理員按角色分配：

| 角色 | 能做的事（摘要） |
|------|------|
| 讀取（Read） | 檢視與討論專案 |
| 分類（Triage） | 管理問題與提取要求，但不能寫入程式碼 |
| 寫入（Write） | 向存放庫推送內容 |
| 維護（Maintain） | 管理存放庫，但不能進行敏感或破壞性操作 |
| 管理（Admin） | 完整權限，含刪除存放庫等操作 |

> [!warning] 沒有寫入權限時，改動透過提取要求提交或交由維護者處理；無法確定權限時按唯讀方式操作，不要探測或繞過權限限制。

### 名詞速查

| 名詞 | 含義（一句話） |
|------|----------------|
| 存放庫（Repository） | 專案檔案與完整歷史記錄的儲存位置 |
| 提交（Commit） | 一次帶說明的修改快照，構成歷史記錄 |
| 分支（Branch） | 存放庫內的並行開發線，改動先落在分支上 |
| 複製（Clone） | 將存放庫完整下載到本機電腦 |
| 分叉（Fork） | 將他人的存放庫複製一份到自己帳號下，改動不影響原存放庫 |
| 提取要求（Pull Request，PR） | 請求審查並合併某分支改動的機制，協作的核心 |
| 問題（Issue） | 提問、回報錯誤、建議的討論串 |
| 發行版（Release） | 標上版本號的正式發布，附可下載檔案（如指南 PDF） |
| 星號（Star） | 收藏與按讚，也用於判斷專案人氣 |
| 關注（Watch） | 訂閱存放庫的動態通知 |
| Actions | GitHub 的自動化管線（本專案用於建置與發布網站） |
| Pages | GitHub 的靜態網站代管（本專案網站即由此發布） |
| README | 存放庫首頁的說明文件，應先閱讀 |

### 團隊存放庫地圖

| 存放庫 | 說明 | 修改方式 |
|------|------|----------|
| `quick-start-guide` | 指南原始檔、建置腳本與網站產物（公開） | 提交提取要求，或交由維護者處理 |
| `ftc32477.github.io` | 團隊網站發布存放庫（公開），內容由各來源存放庫自動推送 | 不直接修改 |
| `.github` | 組織首頁資料，如組織簡介（公開） | 提交提取要求，或交由維護者處理 |
| `FTC-32477-<賽季>-Program` | 賽季程式存放庫（公開）：每賽季單獨建立，舊賽季封存為唯讀；新賽季存放庫建立後補充具體名稱 | 按程式組內部分工 |

> [!danger] **發布存放庫禁區**：`ftc32477.github.io` 的所有內容均來自各自的來源存放庫，由 GitHub Actions 自動推送；直接修改會在下一次推送時被覆蓋。不要在該存放庫或任何產生的內容上點擊編輯、提交或刪除。網站問題一律回到對應來源存放庫處理（本指南為 `quick-start-guide`）。

### 瀏覽與下載

1. 開啟組織首頁 [https://github.com/ftc32477](https://github.com/ftc32477)，在 Repositories 清單中進入存放庫
2. 先讀存放庫首頁的 **README**（專案用途、使用方法）；右側 About 區有簡介與首頁連結
3. 頂部頁籤（是否可見取決於權限）：
   - **Code**：檔案清單與提交歷史
   - **Issues**：問題與建議
   - **Pull requests**：待審查的改動
   - **Actions**：自動化建置與發布記錄
   - **Releases**：正式版本與下載檔案
4. 下載整個存放庫：Code → **Download ZIP**
5. 下載指南 PDF：進入 **Releases**，選擇版本，在 Assets 中下載對應語言
6. 檢視歷史：Code 頁的 **Commits** 清單 → 點進單次提交檢視具體改動（diff）

### 回報問題（Issue）

遇到故障、文件錯誤或有建議時，用 Issue 回報：

1. 開啟目標存放庫的 **Issues** 頁籤，先搜尋是否已有相同問題
2. 點擊 **New issue**，用一句話標題說明問題
3. 正文寫清：**發生了什麼**、**期望的結果**、**如何重現**（步驟）、相關截圖（先移除個人資訊）
4. 提交後關注回覆；問題解決後由維護者關閉

> [!info] 指南的固定回報入口：[https://github.com/ftc32477/quick-start-guide/issues](https://github.com/ftc32477/quick-start-guide/issues)

### 網頁端修改（編輯 → 提 PR）

沒有寫入權限時，GitHub 會自動把網頁端改動做成「分叉（Fork）+ 提取要求（PR）」：

1. 登入後開啟要修改的檔案（如指南 `src/zh-hans/` 下的某篇 `.md`）
2. 點擊檔案右上角的鉛筆圖示 **Edit this file**
3. 若無寫入權限，頁面會提示將自動建立分叉，同意即可
4. 修改內容，在 **Commit changes** 中填寫一句清楚的說明
5. 選擇 **Create a new branch for this commit and start a pull request**，分支名如 `fix/typo-member`
6. 在開啟的 PR 表單中說明修改內容與原因，點擊 **Create pull request**
7. 等待維護者審查；如有評論，按意見繼續修改，合併後改動即生效

> [!warning] 一次 PR 只提交一件事；不要修改不熟悉的檔案（建置腳本、自動產生的檔案等）；發布存放庫不提交任何改動。

### 本機協作

在本機複製存放庫進行開發是最常用的方式。前提是本機已安裝 Git（見「二、環境配置」）。常用指令如下：

```bash
# 將存放庫複製到本機
git clone https://github.com/ftc32477/quick-start-guide.git
cd quick-start-guide

# 開始工作前先拉取最新改動
git pull

# 為本次工作建立新分支
git switch -c feat/my-feature

# 修改檔案後：檢視狀態、暫存、提交
git status
git add <檔案>
git commit -m "本次修改說明"

# 推送分支到 GitHub
git push -u origin feat/my-feature
```

推送後，在 GitHub 上為該分支建立 Pull Request，等待審查合併。Android Studio 與 Visual Studio Code 提供等效的圖形化操作（見「二、環境配置」），可用介面完成相同步驟。

> [!warning] 三條紀律：**先 pull 再動手**；**一次提交只做一件事、說明寫清楚**；**推送到自己的分支，不直接推 main**。

**分叉與上游同步（參與外部專案時）**：分叉的存放庫不會自動更新。需要先將原存放庫新增為上游：`git remote add upstream <原存放庫網址>`，再用 `git fetch upstream` 與合併操作同步（詳見官方文件「同步分叉」一節）。

### 開源社群（搜尋、評估與貢獻）

**搜尋**（搜尋框支援限定詞，可組合使用）：

- `topic:ftc`、`topic:first-tech-challenge`、`topic:ftc-robot`：FTC 社群專案的總入口
- `ftc language:Java sort:updated`：最近仍在維護的 Java 專案
- `"FIRST Tech Challenge" in:readme`：README 中提及 FTC 的專案

FTC 常用開源資源（均可在 GitHub 找到）：

| 專案 | 用途 |
|------|------|
| FIRST-Tech-Challenge/FtcRobotController | FTC 官方 SDK 與範例 |
| FTCLib/FTCLib | FTC 常用工具庫 |
| acmerobotics/road-runner | 動作規劃與路徑跟隨 |
| Pedro-Pathing/PedroPathing | 路徑規劃 |
| acmerobotics/ftc-dashboard | 除錯儀表板 |
| OpenFTC/EasyOpenCV | 視覺處理 |
| the-orange-alliance、ftc-scout/ftc-scout | 賽事資料與統計 |

**評估一個存放庫是否可用（五看）**：最近提交時間（是否仍在維護）、README 與文件品質、授權條款（License）、Issues 活躍度、Releases 有無正式版本。

**授權條款速覽**（使用他人的程式碼或素材前必看）：

| 授權條款 | 一句話說明 |
|--------|------------|
| MIT | 最寬鬆：保留版權聲明即可自由使用 |
| Apache-2.0 | 同樣寬鬆，另有專利授權與變更聲明要求 |
| GPL-3.0 | 具有傳染性：基於它的衍生作品也須開源 |
| 無授權條款 | 預設「保留所有權利」，**不能**直接複製使用，需先聯絡作者 |

**參與貢獻**：先閱讀專案根目錄的 `CONTRIBUTING.md`（貢獻指南）與行為準則；不確定的改動先開 Issue 討論；小修小補按上文「編輯 → 提 PR」流程提交。

> [!warning] 安全：不要執行來源不明的腳本或執行檔；不要把 API Key、密碼、Token 發到 Issue 或存放庫中；對 `curl | bash` 一類的安裝指令保持警覺。

### 危險操作警示

> [!danger] 以下操作可能造成不可逆的損失，一般隊員一律不要執行；確有需要時先經管理員確認。
>
> - 直接修改發布存放庫 `ftc32477.github.io`（會被覆蓋並污染正式網站）
> - `git push --force`：強制覆蓋遠端歷史，可能讓隊友的提交消失
> - `git reset --hard`：捨棄本機未推送的改動，且難以找回
> - 刪除分支、刪除存放庫，或修改存放庫的可見性、名稱、歸屬
> - 向存放庫提交金鑰、密碼、Token（一旦公開，即使刪除仍會留在歷史記錄中，必須立即撤銷並重建）
> - 在 Issue、PR 或公開存放庫中發布內部資料與私人資訊（電子郵件、住址、截圖中的個人資訊）
> - 執行或合併來源不明的程式碼

> [!info] 帳號安全：不要與他人共用帳號；GitHub 正在對參與程式碼貢獻的帳號強制要求啟用兩步驟驗證（2FA），請按提示開啟；個人存取權杖（Token）按最小權限建立，且絕不寫入程式碼或存放庫。

### 練習清單

1. 開啟組織首頁，進入 `quick-start-guide` 存放庫，用 README 說出這個專案是做什麼的
2. 在 Releases 中下載任一種語言的指南 PDF
3. 在提交歷史中找到最近一次修改，說出它改了什麼
4. 在 Issues 中搜尋「PDF」，看看有沒有相關問題
5. 按「編輯 → 提 PR」流程修正一處錯別字，並提交一個提取要求

### 官方文件入口

需要更深入的用法時，按需查閱以下官方文件：

- GitHub 快速入門：[https://docs.github.com/zh/get-started/quickstart](https://docs.github.com/zh/get-started/quickstart)
- 編寫與儲存程式碼（分支/提交/PR）：[https://docs.github.com/zh/get-started/start-your-journey/writing-and-storing-your-code](https://docs.github.com/zh/get-started/start-your-journey/writing-and-storing-your-code)
- Git 速查表：[https://docs.github.com/zh/get-started/git-basics/git-cheatsheet](https://docs.github.com/zh/get-started/git-basics/git-cheatsheet)
- 搜尋語法：[https://docs.github.com/zh/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax](https://docs.github.com/zh/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax)
- GitHub 組織的存放庫角色：[https://docs.github.com/zh/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization](https://docs.github.com/zh/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization)
- 互動式課程（英文）：[https://skills.github.com/](https://skills.github.com/)

> [!info] 遇到不確定的操作，先諮詢管理員或在 Issues 中提問。
