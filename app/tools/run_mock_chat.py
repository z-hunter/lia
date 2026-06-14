from app.cognition.conversation_manager import ConversationManager
from app.llm.clients import MockLocalLLMClient
from app.memory.db import connect, initialize
from app.memory.repository import MemoryRepository
from app.memory.retriever import MemoryRetriever
from app.personality.relationship_model import RelationshipStore
from app.personality.state import PersonalityStateStore


def main():
    conn = connect(); initialize(conn); repo = MemoryRepository(conn)
    manager = ConversationManager(
        repo,
        PersonalityStateStore(repo),
        RelationshipStore(repo),
        MemoryRetriever(repo),
        MockLocalLLMClient(),
    )
    print(manager.handle_user_message("I want memory and continuity to shape this personality.", "cli_mock"))


if __name__ == "__main__":
    main()
