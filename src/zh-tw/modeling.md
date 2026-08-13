# 建模設計

## 一、基本資料

以下是建模設計需要追加的資料。

### 應用程式

- 網路瀏覽器（Chrome 或 Edge 或 Safari）
- LocalSend
- Onshape FTC 零件庫 — [https://ftconshape.com/](https://ftconshape.com/)（FIRST 與 PTC 合作維護；發郵件至 FIRST@ptc.com 可加入共享資料夾）
- FTC Insert Tool 零件庫外掛 — [https://cad.onshape.com/appstore/apps/Design%20&%20Documentation/6515cfb91574253b1b96a6ba](https://cad.onshape.com/appstore/apps/Design%20&%20Documentation/6515cfb91574253b1b96a6ba)（Onshape 應用程式商店安裝：Subscribe → Get for Free）

### 線上帳戶

- CycleZLab — [https://www.cyclezlab.com/](https://www.cyclezlab.com/)（免費，需申請加入）

---

## 二、環境配置

以下是在正式開始前需要配置的工作環境，請按照說明操作。如有疑問，請向管理員諮詢。

### 網路瀏覽器

需要追加收藏儲存的網址如下：

| 名稱 | 網址 |
|------|------|
| goBILDA | https://www.gobilda.com/ |
| REV Robotics | https://www.revrobotics.com/ |
| CycleZLab | https://www.cyclezlab.com/ |

---

## 三、建模設計要點

### 零件設計與裝配

在 Onshape 中進行 3D 建模時，需要特別注意以下幾點：

- **尺寸精度**：確保模型中所有尺寸與實際零件一致
- **裝配關係**：合理設定零件之間的裝配配合（Mate 與 Mate Connector）
- **干涉檢查**：在裝配完成後進行干涉檢查
- **零件命名**：按照統一規範命名零件和裝配體

### FTC 常用零件庫

常用的 FTC 零件供應商與資源平台：

- **goBILDA**：提供完整的 FTC 結構件
- **REV Robotics**：提供電控模組和結構件
- **CycleZLab**：FIRST 機器人社群平台（CAD、程式碼與建造日誌檔案庫）

### 設計規範

- 使用公制單位（mm）
- 所有 3D 列印件需預留適當的間隙（推薦 0.2-0.3mm）
- 匯出格式：STEP 檔案用於加工，STL 檔案用於 3D 列印，3MF 檔案用於切片列印
