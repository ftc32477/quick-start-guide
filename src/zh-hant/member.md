# 隊員須知

## 一、基本資料

以下是所有隊員均需準備的資料。

### 設備

以下選項任一即可：

- 搭載 Windows 10 及以上的電腦
- 搭載 macOS 13 及以上的電腦

### 網路環境

需要能夠存取 Android 支援資源的網路環境。

- Android 支援：[https://support.google.com/android](https://support.google.com/android)

> [!info] 隊伍自建區域網路接入校園獨立閘道，穩定性高於一般校園網路，但仍受校園網路的存取限制。程式設計需要存取 Android 支援的境外網路資源，隊伍可提供存取途徑；如有大流量需求，建議自行購買服務。

### 應用程式

- 網路瀏覽器（Chrome 或 Edge 或 Safari）
- LocalSend

### 線上帳戶

- 電子郵件（推薦使用 @gmail.com 或 @outlook.com）
  - 建立 Gmail 帳號：[https://support.google.com/mail/answer/56256](https://support.google.com/mail/answer/56256)
  - 建立 Outlook 帳號：[https://outlook.live.com/mail/?prompt=create_account](https://outlook.live.com/mail/?prompt=create_account)
- GitHub — [https://github.com/](https://github.com/)
- Onshape — [https://www.onshape.com/](https://www.onshape.com/)

> [!warning] 除此之外，建模設計、結構建造、程式設計、外部聯絡均有各自需要追加的資料。

---

## 二、環境配置

以下是在正式開始前需要配置的工作環境，請按照說明操作。如有疑問，請向管理員諮詢。

### 網路瀏覽器

自行安裝即可，推薦使用 Chrome。

Chrome 下載地址：[https://www.google.com/chrome/](https://www.google.com/chrome/)

**需要了解、閱讀並儲存的網址如下：**

| 名稱 | 網址 |
|------|------|
| Current Game and Season Materials | https://ftc-resources.firstinspires.org/ftc/game |
| FIRST Tech Challenge documentation | https://ftc-docs.firstinspires.org/en/latest/index.html |
| FTC AI | https://ftc-cmchatbot.firstinspires.org/ |
| Techno Trojans | https://www.fruitportrobotics.org/ |
| FTC Event Web — Team 32477 | https://ftc-events.firstinspires.org/team/32477 |
| 32477 — FTCScout | https://ftcscout.org/teams/32477 |
| GitHub FTC 32477 | https://github.com/ftc32477 |

### 網路環境

#### 區域網路

工作區配備有線和無線區域網路，無線區域網路名稱為 `BNDES-FTC`，閘道器為 `192.168.3.1`，無線網路標準為 802.11ax。

密碼請諮詢管理員。

#### 網際網路

具體操作請諮詢管理員。

### LocalSend

LocalSend 是我隊採用的區域網路檔案傳輸工具。

**安裝流程（以 v1.18.2 版本為例）：**

> [!warning] 對於 **iOS** 系統：開啟 [https://apps.apple.com/us/app/localsend/id1661733229](https://apps.apple.com/us/app/localsend/id1661733229) 安裝即可。

1. 開啟 [https://localsend.org/zh-CN/download](https://localsend.org/zh-CN/download)
2. 或進入 GitHub 存放庫：[https://github.com/localsend/localsend/releases](https://github.com/localsend/localsend/releases)
3. 下滑頁面，在最新版本的視窗下的 Assets 清單中點擊「Show all assets」來顯示所有可用版本
4. 下載對應版本並安裝即可

**各平台版本說明：**

- **Android 系統：**
  - `-android-arm32v7.apk`：針對 32 位元 ARM 第 7 代 CPU 架構所建置的版本
  - `-android-arm64v8.apk`：針對 64 位元 ARM 第 8 代 CPU 架構所建置的版本
  - `-android-google-play.apk`：針對 Google Play 商店所建置的版本（可能需要 Google Mobile Services 支援）
  - `-android-x64.apk`：針對 64 位元 x86 架構所建置的版本
- **Linux 系統：**
  - `-linux-arm-64.deb`：針對 64 位元 ARM 架構 Debian/Ubuntu 等系統所建置的 Deb 安裝套件版本
  - `-linux-arm-64.tar.gz`：針對 64 位元 ARM 架構 Linux 系統所建置的通用壓縮套件版本
  - `-linux-x86-64.AppImage`：針對 64 位元 x86 架構 Linux 系統所建置的 AppImage 可執行版本
  - `-linux-x86-64.deb`：針對 64 位元 x86 架構 Debian/Ubuntu 等系統所建置的 Deb 安裝套件版本
  - `-linux-x86-64.tar.gz`：針對 64 位元 x86 架構 Linux 系統所建置的通用壓縮套件版本
- **Windows 系統：**
  - `-windows-x86-64.exe`：針對 64 位元 x86 架構所建置的安裝程式版本
  - `-windows-x86-64.zip`：針對 64 位元 x86 架構所建置的免安裝壓縮套件版本
- **macOS 系統：**
  - `.dmg`：針對 macOS 系統所建置的磁碟映像安裝套件版本

### GitHub

GitHub 是我隊採用的程式碼與資料代管平台。

**註冊流程：**

1. 開啟 [https://github.com/signup](https://github.com/signup)
2. 按照提示建立個人帳戶
   - 註冊期間，系統會要求驗證電子郵件地址
   - 建議將國家/地區選項選擇為「美國」
3. 註冊完成後，請向管理員告知你的使用者名稱，並等待管理員向你發來加入組織邀請。你可以在 [https://github.com/notifications](https://github.com/notifications) 查收。

加入組織後，即可在 [https://github.com/orgs/ftc32477/repositories](https://github.com/orgs/ftc32477/repositories) 檢視組織存放庫；如需修改內容，按《程式設計》「五、GitHub 協作基礎」的流程提交提取要求。

**參考資料：**

- [GitHub 建立帳戶文件](https://docs.github.com/zh/get-started/start-your-journey/creating-an-account-on-github)

### Onshape

Onshape 是我隊採用的雲端 3D 建模平台。

全隊 Onshape 帳號均使用免費的教育版（Education Plan）。

**註冊流程：**

1. 開啟教育版註冊頁：[https://www.onshape.com/en/education/sign-up](https://www.onshape.com/en/education/sign-up)
2. 填寫註冊表單並提交即可

參考資料：

- [Onshape 教育版計畫說明](https://www.onshape.com/en/education/plans)

---

## 三、賽季與活動安排

### 賽季時間線

- FTC 賽季從當年 9 月中旬的 Kickoff 開始，至次年 4 月下旬至 5 月初的 FIRST Championship（休士頓）；官方支援通常延續至當年 7 月底。新賽季賽題隨 Kickoff 發布，此後進入機器人設計與調試階段
- 資格賽在全國多個城市設置分賽場；資格賽晉級後可在寒假參加全國賽事，再晉級可赴美國休士頓參加國際總決賽（截至 2026 年，中國大陸僅約 4 支隊伍晉級過休士頓總決賽）
- 新賽季基礎場地材料在開學後由官方統一配送，到貨後即可搭建新賽季場地

### 賽事規則須知

- 參賽機器人使用有線手把手動操控（如 Logitech F310、Xbox 360）；官方要求必須為有線連接，允許型號以當季《競賽手冊》為準
- 規則禁止使用繼電器、電磁鐵與電磁螺線管（R506）；普通永磁磁鐵可作為原材料使用（R302）
- FTC 官方參賽年齡範圍為 12–18 歲，國中生也可參加
