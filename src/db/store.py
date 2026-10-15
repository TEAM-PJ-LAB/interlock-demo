"""In-memory tables. Swap for a real database later; the interface stays the same."""

from __future__ import annotations

import itertools
from typing import Any

_tables: dict[str, dict[int, dict[str, Any]]] = {}
_ids = itertools.count(1)


def insert(table: str, row: dict[str, Any]) -> dict[str, Any]:
    row = {"id": next(_ids), **row}
    _tables.setdefault(table, {})[row["id"]] = row
    return row


def get(table: str, row_id: int) -> dict[str, Any] | None:
    return _tables.get(table, {}).get(row_id)


def find(table: str, **where: Any) -> list[dict[str, Any]]:
    return [r for r in _tables.get(table, {}).values() if all(r.get(k) == v for k, v in where.items())]


def update(table: str, row_id: int, **changes: Any) -> dict[str, Any]:
    row = _tables[table][row_id]
    row.update(changes)
    return row


def reset() -> None:
    _tables.clear()
