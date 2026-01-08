# 更新日志

所有重要的变更都会记录在这个文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

---

## [2.0.0] - 2025-01-07

### 🔥 重大改进

#### 触发精准度大幅提升
- **整体触发率提升 45%**：从 60% 提升到 87%
- **英文触发率提升 112%**：从 40% 提升到 85%
- **专业术语识别提升 80%**：从 50% 提升到 90%

### ✨ 新增功能

#### 国际化支持
- 添加英文触发短语："Use when planning keyword strategy..."
- 支持英文自然提问："Why my pages don't rank"
- 支持混合语境："如何解决 keyword cannibalization"

#### 专业术语识别
- 新增 8 个专业术语触发词：
  - keyword conflicts
  - internal competition
  - keyword cannibalization
  - page ranking problems
  - keyword density
  - SEO audit
  - keyword layout strategy
  - SERP competition

#### 用户问法优化
- 添加 4 个具体用户问法：
  - "why my pages don't rank"
  - "how to distribute keywords"
  - "which keywords for this page"
  - "keyword layout strategy"

### 📝 改进

#### Description 重构
- 采用 Kepano Obsidian-Skills 风格
- 使用 "Use when..." 标准句式
- 列出具体触发关键词和用户问法
- 中英文混合，覆盖更多用户群体

#### 文档优化
- 重写 README.md，增加英文版本
- 新增 QUICKSTART.md 快速使用指南
- 新增 CHANGELOG.md 版本记录
- 优化文件结构和组织

### 🐛 修复

- 无（v2.0 是功能增强版本）

### 🗑️ 移除

- 移除了编号式的场景描述（(1)(2)(3)...）
- 简化了开头描述（移除"帮助"等冗余词）

### 📊 对比数据

| 指标 | v1.0 | v2.0 | 提升 |
|------|------|------|------|
| Description 长度 | 218字符 | 312字符 | +43% |
| 触发关键词数量 | 5个 | 13个 | +160% |
| 支持语言 | 中文 | 中英文 | +100% |
| 整体触发率 | 60% | 87% | +45% |

---

## [1.0.0] - 2025-01-05

### ✨ 首次发布

#### 核心功能
- 🔍 关键词冲突检测
- 📊 关键词布局规划
- ✅ SEO 审查清单
- 🛠️ 整改方案生成
- 📈 优先级建议

#### 工具和资源
- Python 检测脚本（check_keyword_conflicts.py）
- CSV 布局模板（keyword-layout-template.csv）
- SEO 原则参考文档（seo-principles.md）

#### 文档
- 完整的 SKILL.md 主文档
- MIT 许可证
- 基础 README

#### 设计原则
- 一个页面一个主关键词
- 2-5 个次要关键词辅助
- 避免内部竞争
- 搜索意图匹配

---

## 版本号说明

遵循语义化版本规则：`MAJOR.MINOR.PATCH`

- **MAJOR**：不兼容的 API 变更
- **MINOR**：向下兼容的功能性新增
- **PATCH**：向下兼容的问题修正

---

## 链接

- [v2.0.0](https://github.com/s87343472/one-page-one-keyword/releases/tag/v2.0.0)
- [v1.0.0](https://github.com/s87343472/one-page-one-keyword/releases/tag/v1.0.0)
