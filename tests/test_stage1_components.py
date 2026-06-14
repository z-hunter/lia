from datetime import datetime, timezone

from app.cognition.conversation_manager import ConversationManager
from app.cognition.initiative_engine import InitiativeEngine
from app.llm.clients import MockLocalLLMClient
from app.memory.db import connect, initialize
from app.memory.repository import MemoryRepository
from app.memory.retriever import MemoryRetriever
from app.personality.relationship_model import RelationshipStore
from app.personality.state import PersonalityStateStore


def make_repo(tmp_path):
    conn = connect(tmp_path / "agent.sqlite")
    initialize(conn)
    return MemoryRepository(conn)


def test_retriever_and_mock_conversation_create_continuity_records(tmp_path):
    repo = make_repo(tmp_path)
    state = PersonalityStateStore(repo); state.save(state.load())
    relationship = RelationshipStore(repo); relationship.save(relationship.load())
    manager = ConversationManager(repo, state, relationship, MemoryRetriever(repo), MockLocalLLMClient())

    reply = manager.handle_user_message("Memory and continuity matter here.", "test")
    context = MemoryRetriever(repo).build_context("continuity")

    assert "Mock thought" in reply
    assert context.beliefs
    assert context.open_threads
    assert len(context.recent_events) >= 2


def test_initiative_engine_respects_daily_limit(tmp_path, monkeypatch):
    monkeypatch.setenv("MAX_PROACTIVE_MESSAGES_PER_DAY", "1")
    repo = make_repo(tmp_path)
    repo.upsert_thread("continuity follow-up", .9, .9, .1, "draft")
    repo.add_proactive("existing", "already created today", .5)

    assert InitiativeEngine(repo).run_once() is None
