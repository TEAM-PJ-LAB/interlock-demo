# interlock-demo

A small shop backend used to demonstrate [Interlock](https://github.com/TEAM-PJ-LAB/yc): several AI
coding agents change this repository in parallel, and Interlock keeps them from editing the same
files at the same time.

```
src/auth/      sessions, passwords, require_login
src/billing/   customers, payment webhooks
src/api/       order handlers
src/db/        in-memory store, migrations
```

```bash
python -m pytest -q
```

Agents follow the rules in [AGENTS.md](AGENTS.md).
