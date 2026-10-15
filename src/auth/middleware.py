"""Guards for request handlers."""

from __future__ import annotations

from collections.abc import Callable
from functools import wraps
from typing import Any

from .session import get_session


class Unauthorized(Exception):
    pass


def require_login(handler: Callable[..., Any]) -> Callable[..., Any]:
    """Resolve `headers["Authorization"] = "Bearer <token>"` into `user_id` for the handler."""

    @wraps(handler)
    def wrapper(headers: dict[str, str], *args: Any, **kwargs: Any) -> Any:
        token = headers.get("Authorization", "").removeprefix("Bearer ").strip()
        session = get_session(token) if token else None
        if session is None:
            raise Unauthorized("login required")
        return handler(session.user_id, *args, **kwargs)

    return wrapper
