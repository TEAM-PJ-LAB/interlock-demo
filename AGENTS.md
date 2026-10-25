# Working in this repository

<!-- interlock:begin -->
## Interlock

Several agents work on this repository at the same time. Interlock claims the files your task names
when it starts and releases them when your session ends; call `claim_files` only for other code you
will change. An edit that overlaps another agent's work is refused once: fit your change to its intent
and retry (or `wait_for_files`); never end a task only because of a refusal. Before changing a
function's signature, declare it with `declare_contract`. A signature shown with an "Interlock:" note
is a peer's declared change: write the calls you add for it, and leave its existing calls and tests to
that peer. When you finish, fix what Interlock reports (calls that do not fit a peer's change, tests
failing merged with a peer's work), then finish.
<!-- interlock:end -->

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
