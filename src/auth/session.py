"""Login sessions: email + password in, opaque bearer token out."""

from __future__ import annotations

import secrets
import time
from dataclasses import dataclass

from db import store

from .passwords import hash_password, verify_password

SESSION_TTL_S = 7 * 24 * 3600


@dataclass(frozen=True)
class Session:
    token: str
    user_id: int
    expires_at: float


class LoginError(Exception):
    pass


def register(email: str, password: str) -> dict:
    if store.find("users", email=email.lower()):
        raise LoginError("email already registered")
    return store.insert("users", {"email": email.lower(), "password_hash": hash_password(password)})


def login(email: str, password: str) -> Session:
    users = store.find("users", email=email.lower())
    if not users or not verify_password(password, users[0]["password_hash"]):
        raise LoginError("wrong email or password")
    return _start(users[0]["id"])


def _start(user_id: int) -> Session:
    session = Session(secrets.token_urlsafe(32), user_id, time.time() + SESSION_TTL_S)
    store.insert("sessions", {"token": session.token, "user_id": user_id, "expires_at": session.expires_at})
    return session


def get_session(token: str) -> Session | None:
    rows = store.find("sessions", token=token)
    if not rows or rows[0]["expires_at"] < time.time():
        return None
    return Session(rows[0]["token"], rows[0]["user_id"], rows[0]["expires_at"])


def logout(token: str) -> None:
    for row in store.find("sessions", token=token):
        store.update("sessions", row["id"], expires_at=0)
