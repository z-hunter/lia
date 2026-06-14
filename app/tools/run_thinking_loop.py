from app.memory.db import connect, initialize
from app.memory.repository import MemoryRepository
from app.personality.state import PersonalityStateStore
from app.llm.clients import MockLocalLLMClient
from app.cognition.thinking_loop import ThinkingLoop

def main():
    conn=connect(); initialize(conn); repo=MemoryRepository(conn); state=PersonalityStateStore(repo); state.save(state.load())
    if not repo.open_threads(): repo.upsert_thread("persistent artificial personality Stage 1", .8, .9, .1, "think about foundation")
    eid=ThinkingLoop(repo,state,MockLocalLLMClient()).run_once(); print(f"created thought event {eid}")
if __name__ == "__main__": main()
