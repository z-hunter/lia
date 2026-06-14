from __future__ import annotations
from app.memory.repository import MemoryRepository
DEFAULT_RELATIONSHIP={"trust":0.6,"attachment":0.4,"respect":0.5,"intellectual_interest":0.7,"conflict_level":0.0,"shared_history_summary":"","important_shared_topics":[],"sensitive_topics":[],"communication_preferences":[]}
class RelationshipStore:
    def __init__(self, repo:MemoryRepository): self.repo=repo
    def load(self)->dict: return self.repo.get_kv("relationship_state","user") or DEFAULT_RELATIONSHIP.copy()
    def save(self, model:dict)->None: self.repo.set_kv("relationship_state","user",model)
    def update(self, changes:dict)->dict:
        model=self.load(); model.update(changes); self.save(model); return model
