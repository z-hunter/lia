from __future__ import annotations
from app.memory.repository import MemoryRepository
from app.personality.state import PersonalityStateStore
from app.llm.clients import LocalLLMClient
class ThinkingLoop:
    def __init__(self, repo:MemoryRepository, state:PersonalityStateStore, llm:LocalLLMClient): self.repo=repo; self.state=state; self.llm=llm
    def run_once(self)->str:
        st=self.state.load(); threads=self.repo.open_threads(); interests=st.get("current_interests",[])
        topic=(threads[0]["topic"] if threads else (interests[0] if interests else "continuity"))
        out=self.llm.generate_json(f"Think privately about {topic}")
        text=f"Topic: {topic}\n{out.get('text','Mock thought about continuity.')}"
        eid=self.repo.add_event("thinking_loop","internal_thought",text,out.get("importance",0.6),0.1)
        if out.get("task"): self.repo.add_task(out["task"], f"Created from thought about {topic}", "thinking_loop", .45)
        return eid
