# 100 Practical AI CLI Tools 🧰

>  "我建议你做100个项目，也许100个里面会有可以爆款的"

A curated collection of **100 single-file, ultra-pragmatic, no-bullshit AI tools**. 
No complex frameworks, no orchestration hell. Just `stdin` -> `llm` -> `useful output`.

**Goal:** Create one wildly practical developer/sysadmin AI tool per day until we hit 100. Let the community decide which one goes viral.

## The Toolkit

| # | Tool Name | Description | Status |
|---|---|---|---|
| 001 | [git-mind](./001-git-mind) | Automatically reads `git diff` and generates conventional commits. | ✅ Done |
| 002 | [sql-whisper](./002-sql-whisper) | Give it a Postgres/SQLite schema, describe query in English, gets SQL back. | ✅ Done |
| 003 | [json-tamer](./003-json-tamer) | Pipe messy/broken logs/JSON strings. Get perfectly formatted valid JSON out. | ✅ Done |
| 004 | [regex-explainer](./004-regex-explainer) | Paste a cursed Regex. It gives you a human-readable diagram of what it does. | ✅ Done |
| 005 | [docker-healer](./005-docker-healer) | Analyzes `docker ps` and `docker logs`, tells you exactly why a container died. | ✅ Done |
| ... | *95 more coming* | | 🚧 WIP |

## Philosophy
1. **Single File**: Every tool must be a single Python script.
2. **Unix Philosophy**: Read from `stdin`, write to `stdout`. Pipe them together.
3. **Bring Your Own Model**: Always uses `litellm` so you can use `OPENAI_API_KEY` or a free local `ollama`.

## Quick Setup
```bash
git clone https://github.com/zeyuyuyu/100-practical-ai-tools.git
cd 100-practical-ai-tools
pip install litellm rich
```

### License
MIT
