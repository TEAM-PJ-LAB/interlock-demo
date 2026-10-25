# interlock-demo

A small shop backend used to demonstrate [Interlock](https://team-pj-lab.github.io/apps/): several AI
coding agents (Claude Code, Codex, Cursor) change this repository in parallel, and Interlock keeps them
from breaking each other's work, at symbol level rather than file level.

**Watch it:** [79-second demo video](https://team-pj-lab.github.io/apps/#demo). Five agents, one file;
edits that would collide are stopped at the edit, the commit or the merge, each with a reason.

```
src/auth/      sessions, passwords, require_login
src/billing/   customers, payment webhooks
src/api/       order handlers
src/db/        in-memory store, migrations
```

## Try Interlock on this repository

Interlock is in beta. Email pj.southkorea@gmail.com, or use the form on the
[Interlock page](https://team-pj-lab.github.io/apps/#beta), and we reply with the manual and a beta token.
Then, in a clone of this repository:

```bash
interlock init      # sets this clone up for every agent program on this machine
python -m pytest -q # the shop's own tests
```

Start two or more agents on overlapping tasks. Agents follow the rules in [AGENTS.md](AGENTS.md).

## Evidence

Every experiment behind Interlock, with its method, limits and raw data:
[team-pj-lab.github.io/interlock/experiments](https://team-pj-lab.github.io/interlock/experiments/).
