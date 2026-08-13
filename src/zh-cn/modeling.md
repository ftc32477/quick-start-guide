# 建模设计

## 一、基本资料

以下是建模设计需要追加的资料。

### 应用程序

- 网络浏览器（Chrome 或 Edge 或 Safari）
- LocalSend
- Onshape FTC 零件库 — [https://ftconshape.com/](https://ftconshape.com/)（FIRST 与 PTC 合作维护；发邮件至 FIRST@ptc.com 可加入共享文件夹）
- FTC Insert Tool 零件库插件 — [https://cad.onshape.com/appstore/apps/Design%20&%20Documentation/6515cfb91574253b1b96a6ba](https://cad.onshape.com/appstore/apps/Design%20&%20Documentation/6515cfb91574253b1b96a6ba)（Onshape 应用商店安装：Subscribe → Get for Free）

### 在线账户

- CycleZLab — [https://www.cyclezlab.com/](https://www.cyclezlab.com/)（免费，需申请加入）

---

## 二、环境配置

以下是在正式开始前需要配置的工作环境，请按照说明操作。如有疑问，请向管理员咨询。

### 网络浏览器

需要追加收藏保存的网址如下：

| 名称 | 地址 |
|------|------|
| goBILDA | https://www.gobilda.com/ |
| REV Robotics | https://www.revrobotics.com/ |
| CycleZLab | https://www.cyclezlab.com/ |

---

## 三、建模设计要点

### 零件设计与装配

在 Onshape 中进行 3D 建模时，需要特别注意以下几点：

- **尺寸精度**：确保模型中所有尺寸与实际零件一致
- **装配关系**：合理设置零件之间的装配配合（Mate 与 Mate Connector）
- **干涉检查**：在装配完成后进行干涉检查
- **零件命名**：按照统一规范命名零件和装配体

### FTC 常用零件库

常用的 FTC 零件供应商与资源平台：

- **goBILDA**：提供完整的 FTC 结构件
- **REV Robotics**：提供电控模块和结构件
- **CycleZLab**：FIRST 机器人社区平台（CAD、代码与建造日志档案库）

### 设计规范

- 使用公制单位（mm）
- 所有 3D 打印件需预留适当的间隙（推荐 0.2-0.3mm）
- 导出格式：STEP 文件用于加工，STL 文件用于 3D 打印，3MF 文件用于切片打印
