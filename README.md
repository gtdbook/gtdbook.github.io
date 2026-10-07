# 🗂️ gtdbook.github.io — 自运营项目集（showcase）

[gtdbook](https://github.com/gtdbook) 账号的门面站点：一个自动运转的**个人项目集**，
每日扫描账号下的公开仓库，生成可搜索、可筛选、可排序的项目档案页。
不需要人工维护——新仓库建好第二天，就会自动出现在这里。

- 🌐 在线站点：<https://gtdbook.github.io>
- 🧭 与 [self-ops 情报站](https://gtdbook.github.io/self-ops/)（`gtdbook/self-ops`）互为姊妹：
  情报站是体系的大脑（抓情报），本站是体系的橱窗（亮家底）

## 体系架构

```
┌────────────── scan-and-deploy.yml（每日北京时间 08:00）──────────────┐
│                                                                      │
│  扫描 scripts/update_data.py            提交            部署          │
│  ├─ /users/gtdbook        ──►  data.json 有变化  ──►  汇总 4 个静态  │
│  ├─ /users/gtdbook/repos       则提交回仓库          文件到 _site/    │
│  │   （过滤 fork/私有/空仓/                          │               │
│  │     本站自身）                                    ▼               │
│  └─ /repos/…/languages     GitHub Pages 部署（Actions 模式）         │
│      （每仓库语言占比 → 卡片语言条）                                  │
│                                                                      │
│  前端 index.html + style.css + app.js 纯静态：                        │
│  加载 data.json 渲染卡片，支持搜索 / 语言筛选 / 排序 / 双主题          │
└──────────────────────────────────────────────────────────────────────┘
```

## 目录结构

```
index.html                   # 页面骨架（gtdbook 品牌化）
style.css                    # 双主题样式（浅色默认，与情报站同族配色）
app.js                       # 渲染逻辑：搜索 / 语言 chips / 排序 / 主题
scripts/
  update_data.py             # 扫描器：GitHub API → data.json（纯标准库）
data.json                    # 每日自动生成并提交的数据（勿手改）
.github/workflows/
  scan-and-deploy.yml        # 扫描 → 提交 → 部署，一条流水线
```

## data.json 契约

```
owner   { login, name, bio, avatar_url, html_url, followers }
stats   { repos, stars, forks, languages: [{name, count}] }
repos[] { name, description, url, homepage, topics[], language,
          languages: [{name, pct}], stars, forks,
          pushed_at, created_at, archived }
generated_at   ISO 8601（北京时间 08:00 扫描即每日更新）
```

前端只依赖这一个文件；`description`/`topics` 等字段永远有兜底值，
单仓库语言接口失败也不阻塞整体扫描。

## 筛选规则

展示的仓库需同时满足：

- `public`（公开）
- 非 fork
- 非空仓库（`size > 0`）
- 不在排除名单里（`EXCLUDE` 环境变量，默认排除本展示站自身）

## 日常使用

- **看效果**：访问 <https://gtdbook.github.io>，或本地预览：

  ```bash
  python3 -m http.server -d 本仓库目录 8000
  # 浏览器打开 http://127.0.0.1:8000
  ```

- **手动刷新数据**：Actions → 扫描并部署 → Run workflow
- **本地跑扫描器**：`python3 scripts/update_data.py gtdbook`
  （匿名也能跑；带 `GH_TOKEN=xxx` 可绕开 60 次/小时的限速）
- **临时藏起某个仓库**：在 `scan-and-deploy.yml` 的「扫描 GitHub 生成 data.json」
  步骤里加一行 `EXCLUDE: repo-a,repo-b` 环境变量
- **新仓库如何上榜**：正常建仓即可，第二天 08:00 自动出现

## 设计要点

- **零依赖**：扫描器只用 Python 标准库（`urllib`/`json`），没有供应链漂移
- **零密钥**：只用 Actions 内置 `GITHUB_TOKEN`，不存在过期问题
- **自保鲜**：`generated_at` 每日变化 → 每日一次数据提交 → 仓库始终活跃，
  不会触发 GitHub「60 天不活跃自动停用定时任务」机制
- **防循环**：自动提交带 `[skip ci]`，不会再触发部署
- **确定性输出**：排序稳定（最近推送优先，同刻按仓库名），
  数据没变时 diff 干净

## 致谢

本站布局与交互参考了 [szwnba.github.io](https://szwnba.github.io)
（同一用户的另一账号门面站），数据管线按 gtdbook 体系约束用 Python 重写。
