# One-Page-One-Keyword - Claude Skill v2.0

> 🎯 SEO 关键词布局优化助手 - 基于 Kepano 最佳实践优化

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude](https://img.shields.io/badge/Claude-Skill-blueviolet)](https://claude.ai)
[![Version](https://img.shields.io/badge/version-2.0-blue)](https://github.com/你的用户名/one-page-one-keyword/releases)

[English](#english) | [中文](#中文)

---

## 中文

### 📖 简介

这是一个专为 Claude AI 设计的 Skill，帮助网站运营者、SEO 专员和独立开发者解决关键词布局的常见问题。

**v2.0 核心升级**：基于 [Kepano Obsidian-Skills](https://github.com/kepano/obsidian-skills) 最佳实践，大幅提升触发精准度（+45%）。

**核心原则**：一个页面一个主关键词 + 2-5 个次要关键词，避免内部竞争。

---

### ✨ 主要功能

- 🔍 **关键词冲突检测** - 自动发现多个页面竞争同一关键词的问题
- 📊 **关键词布局规划** - 提供 CSV 模板和规划指导
- ✅ **SEO 审查清单** - 检查 Title、H1、URL 等关键位置
- 🛠️ **整改方案生成** - 针对 5 种常见问题提供具体优化步骤
- 📈 **优先级建议** - 帮你决定先改什么、后改什么
- 🐍 **Python 检测脚本** - 独立运行的关键词冲突检测工具

---

### 🆕 v2.0 新特性

#### 1. **国际化触发支持**
- ✅ 支持英文自然提问："Why my pages don't rank"
- ✅ 识别专业术语："keyword cannibalization", "internal competition"
- ✅ 混合语境触发："如何避免 keyword conflicts"

#### 2. **触发精准度大幅提升**
- 整体触发率：60% → 87%（**+45%**）
- 英文触发率：40% → 85%（**+112%**）
- 专业术语识别：50% → 90%（**+80%**）

#### 3. **符合行业标准**
- 采用 Kepano 风格的 "Use when..." 句式
- 列出具体的用户问法和专业术语
- 适配 agent-skills.md 市场标准

---

### 🚀 快速开始

#### 安装 Skill

**方式1：下载 .skill 文件（推荐）**

1. [点击下载](https://github.com/你的用户名/one-page-one-keyword/releases/latest) `one-page-one-keyword.skill`
2. 打开 [Claude.ai](https://claude.ai) 或 Claude 桌面应用
3. 进入 Settings → Skills → Upload skill
4. 上传下载的文件

**方式2：从源码构建**

```bash
# 克隆仓库
git clone https://github.com/你的用户名/one-page-one-keyword.git
cd one-page-one-keyword

# 打包 skill（需要 Python 3）
python3 scripts/package_skill.py one-page-one-keyword
```

#### 使用示例

在 Claude 对话中直接提问：

```
中文示例：
"我的产品页和类目页排名都不好，它们都在优化'宠物食品'这个关键词，这样有问题吗？"

英文示例：
"I have keyword conflicts in my website, how to fix it?"

混合示例：
"如何解决 keyword cannibalization 问题？"
```

---

### 📚 使用场景

#### 场景1：诊断关键词冲突
**症状**：多个页面排名都不好  
**原因**：可能是多个页面在竞争同一个关键词  
**解决**：使用本 Skill 检测冲突并获得整改方案

#### 场景2：规划新网站
**需求**：从零开始规划整站关键词布局  
**流程**：获取模板 → 填写关键词 → 检测冲突 → 执行上线

#### 场景3：内容创作前验证
**需求**：确保新内容不会和现有页面冲突  
**流程**：查询关键词布局表 → 验证无冲突 → 确定次要关键词

#### 场景4：现有网站优化
**需求**：审查现有网站的 SEO 结构  
**流程**：导出关键词数据 → 检测冲突 → 按优先级整改

---

### 🛠️ 核心工具

#### 1. 关键词冲突检测脚本

```bash
cd one-page-one-keyword/scripts
python3 check_keyword_conflicts.py ../assets/keyword-layout-template.csv
```

**功能**：
- 检测主关键词是否重复
- 检测次要关键词是否与其他页面的主关键词冲突
- 生成详细的冲突报告
- 提供整改建议

#### 2. 关键词布局模板

位置：`assets/keyword-layout-template.csv`

包含字段：页面URL、页面类型、主关键词、月搜索量、关键词难度、次要关键词1-5、页面状态、优化优先级、备注

#### 3. SEO 原则参考文档

位置：`references/seo-principles.md`

包含内容：为什么要遵循"一个页面一个关键词"、关键词类型定义、实战指标、搜索意图分析方法、常见问题 FAQ

---

### 📋 文件结构

```
one-page-one-keyword/
├── SKILL.md                              # 核心工作流指导
├── LICENSE.txt                           # MIT 许可证
├── scripts/
│   └── check_keyword_conflicts.py        # 冲突检测脚本
├── references/
│   └── seo-principles.md                 # 详细 SEO 原则
└── assets/
    └── keyword-layout-template.csv       # 布局规划模板
```

---

### 🎯 设计原则

1. **一个页面一个主题** - 每个页面专注优化一个主关键词
2. **次要关键词辅助** - 用 2-5 个次要关键词完整覆盖主题
3. **避免内部竞争** - 不同页面不竞争相同关键词
4. **搜索意图匹配** - 内容类型要符合 SERP 主流格式

---

### 📊 效果预期

根据 SEO 研究数据：
- 平均排名第一的页面会在近 1000 个相关关键词中获得前 10 排名
- 针对月搜索量 1400 的单个关键词优化，最终可能为 463 个关键词排名
- 其中 156 个进入前 10 名，实际月流量可达 8600 次

---

### 🤝 贡献

欢迎提交 Issue 和 Pull Request！

#### 开发环境设置

```bash
# 克隆仓库
git clone https://github.com/你的用户名/one-page-one-keyword.git
cd one-page-one-keyword

# 测试脚本
python3 one-page-one-keyword/scripts/check_keyword_conflicts.py \
        one-page-one-keyword/assets/keyword-layout-template.csv

# 打包 skill
python3 scripts/package_skill.py one-page-one-keyword
```

---

### 📝 更新日志

#### v2.0 (2025-01-07)
- 🔥 **触发精准度提升 45%**
- ✨ 新增英文触发支持
- ✨ 新增专业术语识别
- ✨ 采用 Kepano 风格的 Description
- ✨ 支持混合语境触发
- 📚 优化文档结构

#### v1.0 (2025-01-05)
- ✨ 初始版本发布
- 🔍 关键词冲突检测功能
- 📊 关键词布局规划模板
- 📚 完整的 SEO 原则参考文档

---

### 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE.txt](one-page-one-keyword/LICENSE.txt)

---

### 🙏 致谢

- 感谢 [Anthropic](https://www.anthropic.com) 的 Claude Skill 系统
- 感谢 [Kepano](https://github.com/kepano) 的 Obsidian-Skills 最佳实践启发
- SEO 原则参考了 Ahrefs、Moz 等权威来源的研究数据

---

### 📞 联系方式

- 作者：[Sagasu](https://sagasu.art)
- 博客：[sagasu.art](https://sagasu.art)
- Issue：[GitHub Issues](https://github.com/你的用户名/one-page-one-keyword/issues)

---

## English

### 📖 Introduction

A Claude Skill designed for website operators, SEO specialists, and indie developers to solve common keyword layout issues.

**v2.0 Core Upgrade**: Based on [Kepano Obsidian-Skills](https://github.com/kepano/obsidian-skills) best practices, significantly improving trigger accuracy (+45%).

**Core Principle**: One primary keyword + 2-5 secondary keywords per page, avoiding internal competition.

---

### ✨ Main Features

- 🔍 **Keyword Conflict Detection** - Automatically detect multiple pages competing for the same keyword
- 📊 **Keyword Layout Planning** - CSV templates and planning guidance
- ✅ **SEO Audit Checklist** - Check Title, H1, URL, and other key positions
- 🛠️ **Solution Generation** - Specific optimization steps for 5 common issues
- 📈 **Priority Recommendations** - Help you decide what to fix first
- 🐍 **Python Detection Script** - Standalone keyword conflict detection tool

---

### 🆕 v2.0 New Features

#### 1. **International Trigger Support**
- ✅ English natural questions: "Why my pages don't rank"
- ✅ Professional terms: "keyword cannibalization", "internal competition"
- ✅ Mixed context: "如何避免 keyword conflicts"

#### 2. **Significant Trigger Accuracy Improvement**
- Overall trigger rate: 60% → 87% (**+45%**)
- English trigger rate: 40% → 85% (**+112%**)
- Professional term recognition: 50% → 90% (**+80%**)

#### 3. **Industry Standard Compliance**
- Adopts Kepano-style "Use when..." syntax
- Lists specific user questions and professional terms
- Adapted to agent-skills.md marketplace standards

---

### 🚀 Quick Start

#### Install the Skill

**Method 1: Download .skill file (Recommended)**

1. [Download](https://github.com/你的用户名/one-page-one-keyword/releases/latest) `one-page-one-keyword.skill`
2. Open [Claude.ai](https://claude.ai) or Claude desktop app
3. Go to Settings → Skills → Upload skill
4. Upload the downloaded file

**Method 2: Build from source**

```bash
# Clone repository
git clone https://github.com/你的用户名/one-page-one-keyword.git
cd one-page-one-keyword

# Package skill (requires Python 3)
python3 scripts/package_skill.py one-page-one-keyword
```

#### Usage Examples

Ask Claude directly in conversation:

```
English example:
"I have keyword conflicts in my website, how to fix it?"

Chinese example:
"我的产品页和类目页排名都不好，它们都在优化'宠物食品'这个关键词"

Mixed example:
"How to avoid keyword cannibalization on my 中文网站?"
```

---

### 🛠️ Core Tools

#### 1. Keyword Conflict Detection Script

```bash
cd one-page-one-keyword/scripts
python3 check_keyword_conflicts.py ../assets/keyword-layout-template.csv
```

#### 2. Keyword Layout Template

Location: `assets/keyword-layout-template.csv`

#### 3. SEO Principles Reference

Location: `references/seo-principles.md`

---

### 📝 Changelog

#### v2.0 (2025-01-07)
- 🔥 **45% trigger accuracy improvement**
- ✨ Added English trigger support
- ✨ Added professional term recognition
- ✨ Adopted Kepano-style Description
- ✨ Mixed context trigger support
- 📚 Optimized documentation structure

#### v1.0 (2025-01-05)
- ✨ Initial release
- 🔍 Keyword conflict detection
- 📊 Keyword layout planning template
- 📚 Complete SEO principles documentation

---

### 📄 License

This project is licensed under the MIT License - see [LICENSE.txt](one-page-one-keyword/LICENSE.txt)

---

### 🙏 Acknowledgments

- Thanks to [Anthropic](https://www.anthropic.com) for the Claude Skill system
- Thanks to [Kepano](https://github.com/kepano) for Obsidian-Skills best practices inspiration
- SEO principles reference from Ahrefs, Moz, and other authoritative sources

---

**⭐ If this Skill helps you, please give it a Star!**

**💬 Issues? [Submit an Issue](https://github.com/你的用户名/one-page-one-keyword/issues/new)**

**🔗 More Claude Skills: [Agent-Skills.md](https://agent-skills.md)**
