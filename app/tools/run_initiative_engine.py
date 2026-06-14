from app.memory.db import connect, initialize
from app.memory.repository import MemoryRepository
from app.cognition.initiative_engine import InitiativeEngine


def main():
    conn = connect(); initialize(conn); repo = MemoryRepository(conn)
    proactive_id = InitiativeEngine(repo).run_once()
    print(f"created proactive candidate {proactive_id}" if proactive_id else "no proactive candidate created")


if __name__ == "__main__":
    main()
