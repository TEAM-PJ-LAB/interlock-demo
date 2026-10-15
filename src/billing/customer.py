"""Billing customers: one per user."""

from __future__ import annotations

from db import store


def get_or_create_customer(user_id: int) -> dict:
    existing = store.find("customers", user_id=user_id)
    if existing:
        return existing[0]
    user = store.get("users", user_id)
    if user is None:
        raise KeyError(f"no user {user_id}")
    return store.insert("customers", {"user_id": user_id, "email": user["email"]})
