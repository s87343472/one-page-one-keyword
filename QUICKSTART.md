# 快速使用指南

## 📦 安装 Skill

### 方式1：使用预打包的 .skill 文件

1. 从 [Releases](https://github.com/s87343472/one-page-one-keyword/releases) 下载最新的 `one-page-one-keyword.skill`
2. 打开 Claude.ai 或 Claude 桌面应用
3. 进入 Settings → Skills
4. 点击 "Upload skill" 按钮
5. 选择下载的 .skill 文件

### 方式2：从源码构建

```bash
# 1. 克隆仓库
git clone https://github.com/s87343472/one-page-one-keyword.git
cd one-page-one-keyword

# 2. 打包 skill
python3 scripts/package_skill.py one-page-one-keyword

# 3. 在当前目录会生成 one-page-one-keyword.skill 文件
# 4. 按照方式1的步骤 2-5 上传到 Claude
```

---

## 💬 使用示例

安装后，在 Claude 对话中直接提问即可触发：

### 中文示例

```
我的产品页和类目页都在优化"宠物食品"这个关键词，排名都不好，怎么办？
```

```
我要做一个电商网站，有首页、5个类目页、30个产品页，怎么分配关键词？
```

```
帮我检查这个关键词布局表，看看有没有冲突
[上传你的 CSV 文件]
```

### 英文示例

```
I have keyword conflicts in my website, how to fix it?
```

```
Why my product pages and category pages don't rank well?
```

```
How to plan keyword strategy for a new website?
```

### 混合示例

```
如何解决 keyword cannibalization 问题？
```

```
我的网站需要做 SEO audit，检查 keyword density
```

---

## 🛠️ 使用 Python 检测脚本

Skill 内置了一个 Python 脚本，可以独立运行检测关键词冲突：

### 准备 CSV 文件

1. 复制模板：
```bash
cp one-page-one-keyword/assets/keyword-layout-template.csv my-keywords.csv
```

2. 在 Excel 或 WPS 中编辑 `my-keywords.csv`，填写你的关键词布局

3. 保存为 CSV 格式（UTF-8 编码）

### 运行检测

```bash
cd one-page-one-keyword/scripts
python3 check_keyword_conflicts.py ../assets/my-keywords.csv
```

### 查看报告

脚本会输出详细的冲突报告和整改建议。

---

## 📚 更多文档

- [完整 README](README.md) - 详细功能介绍
- [更新日志](CHANGELOG.md) - 版本历史
- [SEO 原则](one-page-one-keyword/references/seo-principles.md) - 详细的 SEO 原则文档

---

## 🐛 遇到问题？

- 查看 [常见问题](README.md#常见问题)
- 提交 [Issue](https://github.com/s87343472/one-page-one-keyword/issues)
- 访问作者博客：[sagasu.art](https://sagasu.art)

---

## 🎯 快速测试

上传 Skill 后，用这些问法测试是否成功：

✅ 中文测试：`"我有两个页面排名都不好"`  
✅ 英文测试：`"keyword conflicts in my site"`  
✅ 混合测试：`"如何避免 keyword cannibalization"`

全部能触发说明安装成功！
