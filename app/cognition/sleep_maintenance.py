from __future__ import annotations
from app.memory.repository import MemoryRepository
from app.llm.clients import LocalLLMClient
class SleepMaintenance:
    def __init__(self, repo:MemoryRepository, llm:LocalLLMClient): self.repo=repo; self.llm=llm
    def run_once(self)->str|None:
        events=self.repo.unprocessed_events()
        if not events: return None
        ids=[e["id"] for e in events]; joined="\n".join(f"- {e['type']}: {e['text']}" for e in events)
        summary=self.llm.generate(f"Summarize these events into an episode:\n{joined}")
        epi=self.repo.create_episode(summary, ids, importance=max(e["importance"] for e in events), tags=["sleep","reflection"])
        self.repo.add_event("sleep_maintenance","reflection",f"Sleep reflection for {len(ids)} events: {summary}",.6,.05, processed=True)
        self.repo.mark_events_processed(ids)
        return epi
