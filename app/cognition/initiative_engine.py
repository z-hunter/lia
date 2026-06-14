from __future__ import annotations
from datetime import datetime, timedelta, timezone
from app.config import settings
from app.memory.repository import MemoryRepository
class InitiativeEngine:
    def __init__(self, repo:MemoryRepository): self.repo=repo
    def _quiet(self)->bool:
        now=datetime.now().strftime("%H:%M"); s=settings.quiet_hours_start; e=settings.quiet_hours_end
        return s <= now or now < e if s > e else s <= now < e
    def run_once(self)->str|None:
        if not settings.proactive_messages_enabled or self._quiet(): return None
        threads=self.repo.open_threads(); thoughts=self.repo.recent_events(3,"internal_thought")
        if not threads and not thoughts: return None
        topic=threads[0]["topic"] if threads else thoughts[0]["text"].splitlines()[0].replace("Topic: ","")
        text=f"I kept thinking about {topic}. It may be worth revisiting because it connects to our continuity project."
        return self.repo.add_proactive("open_thread_or_recent_thought", text, .6)
