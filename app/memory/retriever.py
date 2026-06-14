from __future__ import annotations

from dataclasses import dataclass
from app.memory.repository import MemoryRepository


@dataclass
class MemoryContext:
    recent_events: list[dict]
    important_events: list[dict]
    beliefs: list[dict]
    open_threads: list[dict]
    relationship: dict | None = None


class MemoryRetriever:
    """Stage-1 retrieval facade.

    This deliberately uses recent/important/keyword SQLite queries for now while
    preserving a replaceable interface for vector or hybrid RAG in later stages.
    """

    def __init__(self, repo: MemoryRepository):
        self.repo = repo

    def build_context(self, query: str = "", limit: int = 8) -> MemoryContext:
        terms = [t.lower() for t in query.split() if len(t) > 2]
        recent = [dict(row) for row in self.repo.recent_events(limit)]
        important = [dict(row) for row in self.repo.important_events(limit)]
        if terms:
            keyword = [dict(row) for row in self.repo.search_events(query, limit)]
            seen = {item["id"] for item in important}
            important.extend(item for item in keyword if item["id"] not in seen)
        return MemoryContext(
            recent_events=recent,
            important_events=important[:limit],
            beliefs=[dict(row) for row in self.repo.list_beliefs("active")[:limit]],
            open_threads=[dict(row) for row in self.repo.open_threads()[:limit]],
            relationship=self.repo.get_kv("relationship_state", "user"),
        )
