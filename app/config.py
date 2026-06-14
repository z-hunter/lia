from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


def _bool(name: str, default: bool) -> bool:
    return os.getenv(name, str(default)).lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    database_path: Path = Path(os.getenv("DATABASE_PATH", "data/agent.sqlite"))
    vault_path: Path = Path(os.getenv("OBSIDIAN_VAULT_PATH", "memory_vault"))
    use_mock_llm: bool = _bool("USE_MOCK_LLM", True)
    use_mock_telegram: bool = _bool("USE_MOCK_TELEGRAM", True)
    use_mock_tools: bool = _bool("USE_MOCK_TOOLS", True)
    timezone: str = os.getenv("TIMEZONE", "Europe/Warsaw")
    quiet_hours_start: str = os.getenv("QUIET_HOURS_START", "23:00")
    quiet_hours_end: str = os.getenv("QUIET_HOURS_END", "09:00")
    proactive_messages_enabled: bool = _bool("PROACTIVE_MESSAGES_ENABLED", True)
    max_proactive_messages_per_day: int = int(os.getenv("MAX_PROACTIVE_MESSAGES_PER_DAY", "3"))
    min_proactive_cooldown_minutes: int = int(os.getenv("MIN_PROACTIVE_COOLDOWN_MINUTES", "120"))


settings = Settings()
