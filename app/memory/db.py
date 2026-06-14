from __future__ import annotations
import sqlite3
from pathlib import Path
from app.config import settings

SCHEMA = Path(__file__).with_name("schema.sql")

def connect(path: Path | None = None) -> sqlite3.Connection:
    db_path = path or settings.database_path
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def initialize(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA.read_text(encoding="utf-8"))
    conn.commit()
