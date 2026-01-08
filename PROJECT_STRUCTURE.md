# 项目结构说明

```
one-page-one-keyword-v2-github/
├── README.md                                 # 项目主页（中英双语）
├── QUICKSTART.md                             # 快速使用指南
├── CHANGELOG.md                              # 版本更新日志
├── CONTRIBUTING.md                           # 贡献指南
├── .gitignore                                # Git 忽略文件
│
├── one-page-one-keyword/                     # Skill 源文件夹
│   ├── SKILL.md                              # 核心 Skill 定义文件
│   ├── LICENSE.txt                           # MIT 许可证
│   ├── scripts/
│   │   └── check_keyword_conflicts.py        # Python 冲突检测脚本
│   ├── references/
│   │   └── seo-principles.md                 # 详细 SEO 原则文档
│   └── assets/
│       └── keyword-layout-template.csv       # 关键词布局 CSV 模板
│
├── scripts/
│   └── package_skill.py                      # 打包脚本（生成 .skill 文件）
│
└── releases/
    └── one-page-one-keyword-v2.0.0.skill     # 预打包的 v2.0 版本
```

## 📂 文件说明

### 根目录文件

| 文件 | 说明 |
|------|------|
| `README.md` | 项目主页，包含完整的功能介绍、安装说明、使用示例（中英双语） |
| `QUICKSTART.md` | 快速使用指南，5 分钟上手 |
| `CHANGELOG.md` | 版本更新历史，记录所有重要变更 |
| `CONTRIBUTING.md` | 贡献指南，欢迎社区参与 |
| `.gitignore` | Git 忽略规则 |

### one-page-one-keyword/ 目录

这是 **Skill 的核心文件夹**，包含所有 Skill 运行所需的文件。

| 文件 | 说明 |
|------|------|
| `SKILL.md` | **最重要的文件**，定义 Skill 的触发条件和工作流程 |
| `LICENSE.txt` | MIT 开源许可证 |
| `scripts/check_keyword_conflicts.py` | Python 检测脚本，可独立运行 |
| `references/seo-principles.md` | 详细的 SEO 原则参考文档（10k+ 字） |
| `assets/keyword-layout-template.csv` | 关键词布局 CSV 模板 |

### scripts/ 目录

项目级别的工具脚本。

| 文件 | 说明 |
|------|------|
| `package_skill.py` | 打包脚本，将 `one-page-one-keyword/` 打包成 `.skill` 文件 |

### releases/ 目录

存放已打包的 `.skill` 文件，方便直接下载使用。

| 文件 | 说明 |
|------|------|
| `one-page-one-keyword-v2.0.0.skill` | v2.0 版本的预打包文件 |

## 🔧 使用流程

### 方式1：直接使用（推荐给普通用户）

1. 下载 `releases/one-page-one-keyword-v2.0.0.skill`
2. 上传到 Claude.ai
3. 开始使用

### 方式2：从源码构建（推荐给开发者）

```bash
# 1. 克隆仓库
git clone https://github.com/你的用户名/one-page-one-keyword.git

# 2. 打包 Skill
cd one-page-one-keyword
python3 scripts/package_skill.py one-page-one-keyword

# 3. 生成 one-page-one-keyword.skill 文件
# 4. 上传到 Claude.ai
```

### 方式3：修改和开发

```bash
# 1. 修改 one-page-one-keyword/ 中的文件
vim one-page-one-keyword/SKILL.md

# 2. 重新打包
python3 scripts/package_skill.py one-page-one-keyword

# 3. 测试新版本
# 上传到 Claude.ai 测试
```

## 📊 文件大小

| 项目 | 大小 |
|------|------|
| 完整项目 | ~50 KB |
| .skill 文件 | ~12 KB |
| Python 脚本 | ~5 KB |
| 文档 | ~30 KB |

## 🎯 关键文件详解

### SKILL.md（最重要）

这是 Claude Skill 的核心定义文件，包含：

1. **YAML Frontmatter**：
   - `name`: Skill 名称
   - `description`: 触发条件（决定何时使用这个 Skill）
   - `license`: 许可证声明

2. **Markdown 正文**：
   - 快速开始
   - 核心原则
   - 工作流程
   - 使用示例
   - 工具说明

### package_skill.py

简单的打包脚本，将 `one-page-one-keyword/` 文件夹打包成 `.skill` 文件。

实际上，`.skill` 文件就是一个 `.zip` 文件，只是扩展名不同。

### check_keyword_conflicts.py

独立的 Python 脚本，可以不依赖 Claude 单独运行，用于检测关键词冲突。

## 🚀 部署到 GitHub

```bash
# 1. 初始化 Git 仓库
cd one-page-one-keyword-v2-github
git init

# 2. 添加所有文件
git add .

# 3. 提交
git commit -m "feat: 发布 v2.0.0 版本"

# 4. 添加远程仓库
git remote add origin https://github.com/你的用户名/one-page-one-keyword.git

# 5. 推送
git push -u origin main
```

## 📦 发布新版本

1. 更新 `CHANGELOG.md`
2. 修改 `one-page-one-keyword/SKILL.md`
3. 重新打包：`python3 scripts/package_skill.py one-page-one-keyword`
4. 重命名为：`one-page-one-keyword-v2.1.0.skill`
5. 移动到 `releases/` 目录
6. 提交并推送
7. 在 GitHub 创建 Release

## 💡 提示

- **不要修改 releases/ 中的文件**，它们是构建产物
- **主要修改 one-page-one-keyword/ 中的文件**，然后重新打包
- **文档和脚本可以直接修改**，无需打包

## 🔗 相关链接

- [Claude Skill 文档](https://docs.anthropic.com/claude/docs/agent-skills)
- [Agent-Skills.md 市场](https://agent-skills.md)
- [Kepano Obsidian-Skills](https://github.com/kepano/obsidian-skills)
