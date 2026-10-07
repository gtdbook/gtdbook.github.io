#!/usr/bin/env python3
"""gtdbook 项目集 · 数据同步脚本

从 GitHub API 拉取指定用户的公开、非 fork 仓库，生成前端使用的 data.json。
只用 Python 标准库，与 gtdbook 体系的「零第三方依赖」约束保持一致。

用法:
    python3 scripts/update_data.py [username]        # 默认 gtdbook
    GH_TOKEN=xxx python3 scripts/update_data.py      # 带令牌可提高速率限制

筛选规则:
    - 仅 public 仓库
    - 排除 fork
    - 排除从未推送过的空仓库（pushed_at 为空；
      不用 size 字段——GitHub 的 size 统计对新建仓库有滞后，常驻 0）
    - 排除 EXCLUDE 环境变量中逗号分隔的仓库名（默认排除本展示站自身）
"""

import http.client
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = "https://api.github.com"
ROOT = Path(__file__).resolve().parent.parent
RETRYABLE = {429, 500, 502, 503}


def build_headers(token):
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "gtdbook-showcase-updater",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


class ApiError(Exception):
    """GitHub API 请求失败（重试后仍失败）。"""


def api(url, headers):
    """GET 一个 GitHub API 端点，瞬时错误（限速/5xx/断连/响应截断）自动重试。"""
    last_err = None
    for attempt in range(3):
        if attempt:
            time.sleep(2 * attempt)
        request = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=30) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as err:
            body = err.read().decode(errors="replace")[:200]
            if attempt < 2 and err.code in RETRYABLE:
                last_err = ApiError(f"GitHub API {err.code}: {url}\n{body}")
                continue
            hint = "（未认证限速 60 次/小时，可在 GH_TOKEN 环境变量提供令牌）" if err.code == 403 else ""
            raise ApiError(f"GitHub API {err.code}: {url}\n{body}\n{hint}")
        except (urllib.error.URLError, OSError, http.client.HTTPException,
                json.JSONDecodeError) as err:
            last_err = ApiError(f"网络错误: {url} ({err})")
    raise last_err


def fetch_repos(owner, headers):
    """分页拉取用户名下全部仓库。"""
    repos, page = [], 1
    while True:
        batch = api(
            f"{API}/users/{owner}/repos?per_page=100&page={page}"
            f"&type=owner&sort=pushed",
            headers,
        )
        repos.extend(batch)
        if len(batch) < 100:
            return repos
        page += 1


def fetch_languages(repo_api_url, headers):
    """单个仓库的语言构成（字节数 -> 百分比），失败不阻塞整体。"""
    try:
        langs = api(f"{repo_api_url}/languages", headers)
    except ApiError:
        return []
    total = sum(langs.values())
    if total <= 0:
        return []
    ranked = sorted(langs.items(), key=lambda kv: (-kv[1], kv[0]))[:5]
    return [
        {"name": name, "pct": round(count / total * 1000) / 10}
        for name, count in ranked
    ]


def main():
    owner = sys.argv[1] if len(sys.argv) > 1 else "gtdbook"
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    exclude = [
        name.strip()
        for name in os.environ.get("EXCLUDE", "gtdbook.github.io").split(",")
        if name.strip()
    ]
    headers = build_headers(token)

    user = api(f"{API}/users/{owner}", headers)

    repos = [
        r for r in fetch_repos(owner, headers)
        if not r["fork"] and not r["private"]
        and r["pushed_at"]  # 从未推送过的空仓库
        and r["name"] not in exclude
    ]

    items = []
    language_count = {}
    total_stars = 0
    total_forks = 0
    for r in repos:
        if r["language"]:
            language_count[r["language"]] = language_count.get(r["language"], 0) + 1
        total_stars += r["stargazers_count"]
        total_forks += r["forks_count"]
        items.append({
            "name": r["name"],
            "description": r["description"] or "",
            "url": r["html_url"],
            "homepage": r["homepage"] or "",
            "topics": r.get("topics") or [],
            "language": r["language"],
            "languages": fetch_languages(r["url"], headers),
            "stars": r["stargazers_count"],
            "forks": r["forks_count"],
            "pushed_at": r["pushed_at"],
            "created_at": r["created_at"],
            "archived": r["archived"],
        })

    # 最近推送在前；同刻推送按名字升序，保证 data.json 可重现
    items.sort(key=lambda x: x["name"])
    items.sort(key=lambda x: x["pushed_at"] or "", reverse=True)
    languages = [
        {"name": name, "count": count}
        for name, count in sorted(
            language_count.items(), key=lambda kv: (-kv[1], kv[0])
        )
    ]

    data = {
        "owner": {
            "login": user["login"],
            "name": user["name"] or user["login"],
            "bio": user["bio"] or "",
            "avatar_url": user["avatar_url"],
            "html_url": user["html_url"],
            "followers": user["followers"],
        },
        "stats": {
            "repos": len(items),
            "stars": total_stars,
            "forks": total_forks,
            "languages": languages,
        },
        "repos": items,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    out = ROOT / "data.json"
    text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    prev = out.read_text(encoding="utf-8") if out.exists() else ""
    out.write_text(text, encoding="utf-8")

    print(f"已扫描 {data['stats']['repos']} 个项目 · {total_stars} Stars · {len(languages)} 种语言")
    print("data.json 已更新" if prev != text else "data.json 未变化")


if __name__ == "__main__":
    try:
        main()
    except ApiError as err:
        raise SystemExit(err)
