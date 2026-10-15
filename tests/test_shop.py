import hashlib
import hmac
import json

import pytest

from api.orders import create_order, list_orders
from auth import LoginError, Unauthorized, login, logout, register
from billing.customer import get_or_create_customer
from billing.webhooks import BadSignature, handle
from db import store


@pytest.fixture(autouse=True)
def clean():
    store.reset()


def auth_headers(email="a@example.com"):
    register(email, "correct horse")
    return {"Authorization": f"Bearer {login(email, 'correct horse').token}"}


def test_login_and_logout():
    h = auth_headers()
    with pytest.raises(LoginError):
        login("a@example.com", "wrong")
    logout(h["Authorization"].removeprefix("Bearer "))
    with pytest.raises(Unauthorized):
        list_orders(h)


def test_orders_are_per_user():
    a, b = auth_headers("a@example.com"), auth_headers("b@example.com")
    order = create_order(a, "keyboard", 2)
    assert order["total_cents"] == 17800 and order["status"] == "pending"
    assert list_orders(a) == [order] and list_orders(b) == []
    with pytest.raises(Unauthorized):
        create_order({}, "mouse")


def test_customer_is_created_once():
    register("c@example.com", "pw")
    user_id = store.find("users", email="c@example.com")[0]["id"]
    assert get_or_create_customer(user_id) == get_or_create_customer(user_id)


def test_payment_webhook_marks_order_paid():
    order = create_order(auth_headers(), "monitor")
    body = json.dumps({"type": "payment.succeeded", "order_id": order["id"]}).encode()
    sig = hmac.new(b"whsec", body, hashlib.sha256).hexdigest()
    assert handle(body, sig, "whsec") == {"handled": True}
    assert store.get("orders", order["id"])["status"] == "paid"
    with pytest.raises(BadSignature):
        handle(body, "0" * 64, "whsec")
