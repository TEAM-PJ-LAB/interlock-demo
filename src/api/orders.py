"""Order handlers. Each takes the request headers first; see auth.require_login."""

from __future__ import annotations

from auth import require_login
from db import store

PRICES_CENTS = {"keyboard": 8900, "mouse": 3900, "monitor": 21900}


@require_login
def create_order(user_id: int, item: str, quantity: int = 1) -> dict:
    if item not in PRICES_CENTS:
        raise ValueError(f"unknown item: {item}")
    if quantity < 1:
        raise ValueError("quantity must be at least 1")
    return store.insert("orders", {"user_id": user_id, "item": item, "quantity": quantity,
                                   "total_cents": PRICES_CENTS[item] * quantity, "status": "pending"})


@require_login
def list_orders(user_id: int) -> list[dict]:
    return store.find("orders", user_id=user_id)
