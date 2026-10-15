CREATE TABLE users (
    id            INTEGER PRIMARY KEY,
    email         TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
);

CREATE TABLE sessions (
    token      TEXT PRIMARY KEY,
    user_id    INTEGER NOT NULL REFERENCES users (id),
    expires_at REAL NOT NULL
);

CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    user_id     INTEGER NOT NULL REFERENCES users (id),
    item        TEXT NOT NULL,
    quantity    INTEGER NOT NULL CHECK (quantity > 0),
    total_cents INTEGER NOT NULL
);

CREATE TABLE customers (
    id      INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL UNIQUE REFERENCES users (id),
    email   TEXT NOT NULL
);
