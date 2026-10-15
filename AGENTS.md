# Working in this repository

Several AI agents work on this codebase at the same time, each on its own branch. They coordinate
through the **interlock** MCP server.

## Rules

1. Before editing any file, call `claim_files` with every file or directory you will change
   (for example `src/auth/` or `src/api/orders.py`) and a one-line `intent`.
2. If the result is `granted: false`, do **not** edit those paths. Tell the user who holds them and
   why (from `conflicts`), then continue with the parts of the task you can do, or wait.
3. Claim only what you need. Prefer files over whole directories when the change is small.
4. After you commit and push, call `release_files`.
5. Use `list_claims` to see what other agents are working on.

## Project

A small shop backend in plain Python (no web framework).

| Path | What it holds |
|---|---|
| `src/auth/` | sessions, password hashing, the `require_login` guard |
| `src/billing/` | customers and payment-provider webhooks |
| `src/api/` | request handlers (orders) |
| `src/db/` | in-memory store and SQL migrations |
| `tests/` | pytest suite |

Run the tests with `python -m pytest -q`.
