from app.memory.db import connect, initialize
from app.memory.repository import MemoryRepository
from app.personality.state import PersonalityStateStore
from app.personality.relationship_model import RelationshipStore
from app.llm.clients import MockLocalLLMClient
from app.cognition.thinking_loop import ThinkingLoop
from app.cognition.sleep_maintenance import SleepMaintenance
from app.cognition.initiative_engine import InitiativeEngine
from app.memory.obsidian_vault import ObsidianVaultWriter


def test_stage1_smoke(tmp_path, monkeypatch):
    monkeypatch.setenv("QUIET_HOURS_START", "23:00")
    monkeypatch.setenv("QUIET_HOURS_END", "00:00")
    conn=connect(tmp_path/"agent.sqlite"); initialize(conn); repo=MemoryRepository(conn)
    state=PersonalityStateStore(repo); state.save(state.load()); state.update({"mood":"curious"})
    rel=RelationshipStore(repo); rel.save(rel.load())
    e1=repo.add_event("test","user_message","The user wants persistent memory and continuity.",.8,.2)
    repo.upsert_belief("user","The user values persistent artificial personality.",.7,[e1])
    repo.upsert_thread("memory as personality substrate",.9,.9,.2,"think privately")
    thought_id=ThinkingLoop(repo,state,MockLocalLLMClient()).run_once()
    episode_id=SleepMaintenance(repo,MockLocalLLMClient()).run_once()
    proactive_id=InitiativeEngine(repo).run_once()
    vault=ObsidianVaultWriter(tmp_path/"vault")
    note=vault.write_note("02_Episodes", episode_id or "none", "Smoke episode", "Continuity smoke test note.", "episode", source_event_ids=[e1, thought_id])
    assert state.load()["mood"] == "curious"
    assert repo.list_beliefs()[0]["status"] == "active"
    assert episode_id is not None
    assert proactive_id is not None
    assert note.exists()
