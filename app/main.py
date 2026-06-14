from app.memory.db import connect, initialize
from app.memory.repository import MemoryRepository
from app.personality.state import PersonalityStateStore
from app.personality.relationship_model import RelationshipStore

def main():
    conn=connect(); initialize(conn); repo=MemoryRepository(conn)
    PersonalityStateStore(repo).save(PersonalityStateStore(repo).load())
    RelationshipStore(repo).save(RelationshipStore(repo).load())
    print("Persistent personality agent started in mock mode.")
if __name__ == "__main__": main()
