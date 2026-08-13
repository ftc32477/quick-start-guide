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

**中文化：**

1. 開啟 [Android Studio 中文語言套件](https://github.com/sollyu/AndroidStudioChineseLanguagePack/releases)
2. 下載最新的語言擴充套件（.jar 檔案）
3. 在主頁面的左側頁籤清單中選擇「Plugins」，選擇「Install Plugin from Disk」
4. 選擇下載的 .jar 檔案並開啟，外掛載入成功後確保其處於開啟狀態
5. 在左側頁籤清單中選擇「Customize」，進入「語言和地區（Language and Region）」，將「語言（Language）」選擇為「Chinese (Simplified) 簡體中文」，將「地區（Region）」選擇為「Americas」，然後重新啟動

**複製存放庫：**

1. 點擊左側頁籤清單中的「GitHub」，點擊「透過 GitHub 登入」進行授權。
2. 選擇當前賽季的程式碼存放庫（如：`ftc32477/FTC-32477-Decode-Program`）
3. 選擇一個不會改變路徑的空資料夾，點擊「複製」
4. 等待檔案下載完成，在左側邊欄的「建置」頁籤或視窗右下透過進度條查看進度

> [!warning] 如有問題，請向管理員諮詢。

### Visual Studio Code

Visual Studio Code 是我隊採用的程式碼編輯與歷史檢視工具。

**軟體安裝及環境配置流程：**

1. 開啟 [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download)
2. 下載對應版本並安裝即可
3. 開啟 [中文化外掛](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans)，安裝該外掛即可中文化。

---

## 三、用品簡介

### Android Studio

官方文件：[https://developer.android.com/studio/intro?hl=zh-cn](https://developer.android.com/studio/intro?hl=zh-cn)

在本專案中，我們基於 FTC 官方提供的應用框架，在 `TeamCode` 資料夾下使用 Java 語言編寫機器人控制程式，以呼叫機器人執行所需的各類依賴庫。

關於 Android Studio 所需掌握的基本知識，請參考官方文件中的簡易頁面指引。

### Visual Studio Code

官方文件：[https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)

鑒於 Visual Studio Code 與 Android Studio 操作邏輯類似，且前者在本專案中使用頻次較低，相關介面指引請參考 Android Studio 部分，此處不再贅述。

### Robot Dashboard

- 連接 Wi-Fi 網路「`32477-RC`」。Wi-Fi 密碼：詢問管理員或透過 Driver Hub 取得。
- 網址是：[http://192.168.43.1:8080/](http://192.168.43.1:8080/)
- 這是 Control Hub 內建的 Wi-Fi 模組的 Web 頁面（官方名稱為 Robot Controller Console，即機器人控制器控制台），提供了管理 Control Hub 的圖形化後台。

關於 Robot Dashboard 所需掌握的基本知識，請參考官方文件中的簡易頁面指引。

---

## 四、工作流程

程式設計組的核心工作分為三部分：

- **自動程式**：賽季自動階段（Auto）的控制邏輯
- **手動程式**：遙控階段（TeleOp）的操作邏輯
- **感測器配置**：各類感測器、視覺系統的配置

### 除錯是核心

> [!info] 程式開發的真正難點在於除錯。自動路徑、手動操作、PID 參數、視覺配置——大部分感測器都有現成的程式套件可以直接複用，你真正要做的是「調」。

除錯工作貫穿整個開發流程：

1. **需求分析**：明確當前賽季的規則和任務需求
2. **架構設計**：設計程式整體架構和模組劃分
3. **程式碼編寫**：在 Android Studio 中編寫 Java 程式碼
4. **版本控制**：使用 Git 進行程式碼版本管理
5. **除錯**：調自動路徑、調手動操作、調 PID 參數、調視覺配置
6. **測試驗證**：在機器人上驗證程式功能
7. **程式碼審查**：透過 GitHub 進行程式碼審查和合併
8. **部署發布**：將最終版本部署到 Robot Controller
