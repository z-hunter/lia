from __future__ import annotations

from app.llm.clients import LocalLLMClient
from app.memory.repository import MemoryRepository
from app.memory.retriever import MemoryRetriever
from app.personality.relationship_model import RelationshipStore
from app.personality.state import PersonalityStateStore


class ConversationManager:
    """Mock-mode conversation pipeline for Telegram or CLI frontends."""

    def __init__(
        self,
        repo: MemoryRepository,
        state: PersonalityStateStore,
        relationship: RelationshipStore,
        retriever: MemoryRetriever,
        llm: LocalLLMClient,
    ):
        self.repo = repo
        self.state = state
        self.relationship = relationship
        self.retriever = retriever
        self.llm = llm

    def handle_user_message(self, text: str, source: str = "telegram_mock") -> str:
        incoming_id = self.repo.add_event(source, "user_message", text, importance=0.5, emotional_valence=0.0)
        context = self.retriever.build_context(text)
        current_state = self.state.load()
        relationship = self.relationship.load()
        prompt = (
            "Reply in mock mode using persistent context.\n"
            f"State: {current_state}\nRelationship: {relationship}\n"
            f"Beliefs: {context.beliefs}\nOpen threads: {context.open_threads}\nUser: {text}"
        )
        reply = self.llm.generate(prompt)
        self.repo.add_event("agent", "agent_message", reply, importance=0.4, processed=False)
        if "memory" in text.lower() or "continuity" in text.lower():
            self.repo.upsert_thread("user is exploring memory and continuity", 0.75, 0.8, 0.1, "ask what continuity should feel like")
            self.repo.upsert_belief("user", "The user is interested in memory-driven continuity.", 0.65, [incoming_id])
        return reply
