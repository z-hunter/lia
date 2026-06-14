from __future__ import annotations
from dataclasses import dataclass, asdict
from app.memory.repository import MemoryRepository

DEFAULT_STATE = {"mood":"neutral","energy":0.6,"curiosity":0.7,"trust_to_user":0.6,"attachment_to_user":0.4,"respect_for_user":0.5,"irritation":0.0,"hurt":0.0,"uncertainty":0.3,"current_interests":["persistent memory","artificial personality"],"current_concerns":[],"self_assigned_goals":["build continuity through memory"],"long_term_questions":["Can continuity emerge from reflection and memory?"]}
class PersonalityStateStore:
    def __init__(self, repo: MemoryRepository): self.repo=repo
    def load(self)->dict: return self.repo.get_kv("personality_state","current") or DEFAULT_STATE.copy()
    def save(self,state:dict)->None: self.repo.set_kv("personality_state","current",state)
    def update(self,changes:dict)->dict:
        st=self.load(); st.update(changes); self.save(st); return st
