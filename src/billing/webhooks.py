"""Incoming payment-provider webhooks, verified with an HMAC-SHA256 signature."""

from __future__ import annotations

import hashlib
import hmac
import json

from db import store


class BadSignature(Exception):
    pass


def handle(body: bytes, signature: str, secret: str) -> dict:
    expected = hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, signature):
        raise BadSignature("signature mismatch")
    event = json.loads(body)
    if event.get("type") == "payment.succeeded":
        order = store.get("orders", int(event["order_id"]))
        if order is not None:
            store.update("orders", order["id"], status="paid")
        return {"handled": True}
    return {"handled": False}
