from __future__ import annotations
from datetime import datetime, timedelta, timezone

from app.config import settings
from app.memory.repository import MemoryRepository


class ProactiveRateLimiter:
    def __init__(self, repo: MemoryRepository):
        self.repo = repo

    def allowed(self) -> bool:
        now = datetime.now(timezone.utc)
        start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
        if self.repo.proactive_count_since(start_of_day) >= settings.max_proactive_messages_per_day:
            return False
        last = self.repo.recent_proactive(1)
        if not last:
            return True
        created = datetime.fromisoformat(last[0]["created_at"])
        cooldown = timedelta(minutes=settings.min_proactive_cooldown_minutes)
        return now - created >= cooldown
