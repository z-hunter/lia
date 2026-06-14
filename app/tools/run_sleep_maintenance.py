from app.llm.clients import MockLocalLLMClient
from app.memory.db import connect, initialize
from app.memory.repository import MemoryRepository
from app.cognition.sleep_maintenance import SleepMaintenance


def main():
    conn = connect(); initialize(conn); repo = MemoryRepository(conn)
    episode_id = SleepMaintenance(repo, MockLocalLLMClient()).run_once()
    print(f"created episode {episode_id}" if episode_id else "no unprocessed events")


if __name__ == "__main__":
    main()
