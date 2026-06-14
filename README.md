# Persistent Artificial Personality — Stage 1 Mock Prototype

This repository contains a Stage 1 foundation for a persistent artificial personality. It is intentionally small, runnable, and mock-first. The personality is represented by persistent memory, beliefs, emotional state, relationship state, open threads, tasks, reflections, and continuity processes — not solely by a system prompt.

## Architecture Overview

Core layers:

- **SQLite operational memory**: events, episodes, beliefs, user profile, self model, open threads, tasks, tool experiences, proactive message candidates, personality state, and relationship state.
- **Personality state**: mood, energy, curiosity, trust, attachment, respect, irritation, hurt, uncertainty, interests, concerns, goals, and long-term questions.
- **Relationship model**: trust, attachment, respect, intellectual interest, conflict level, shared history, topics, sensitivities, and communication preferences.
- **ThinkingLoop**: loads state and open threads, selects a topic, generates a mock private thought, stores it as an event, and may create a task.
- **SleepMaintenance**: collects unprocessed events, creates a mock episode summary, marks source events processed, and records a reflection event.
- **InitiativeEngine**: inspects open threads and recent thoughts, respects quiet hours, and stores proactive message candidates without sending them.
- **Obsidian vault writer**: writes Markdown notes with YAML frontmatter under the configured vault folders.
- **LLM abstractions**: `LocalLLMClient` and `DeepLLMClient` interfaces with mock implementations.
- **Tool abstractions**: web search, Playwright, Google Drive, Docs, Calendar, and Gmail mock interfaces only.
- **Telegram abstraction**: gateway interface plus a mock gateway that prints outgoing messages.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env
```

Stage 1 is designed to run with:

```env
USE_MOCK_LLM=true
USE_MOCK_TELEGRAM=true
USE_MOCK_TOOLS=true
```

No Telegram token, Ollama server, Claude key, Google OAuth, or Playwright install is required.

## Running in Mock Mode

Initialize and start the mock application:

```bash
python -m app.main
```

Run one thinking cycle manually:

```bash
python -m app.tools.run_thinking_loop
```

Run the smoke test:

```bash
pytest
```

## Database Description

The SQLite schema is initialized automatically from `app/memory/schema.sql` and includes:

- `events`: raw user, system, internal thought, and reflection events.
- `episodes`: sleep-consolidated summaries of event groups.
- `beliefs`: statements with confidence, evidence, and status (`active`, `uncertain`, `superseded`).
- `user_profile`: key/value profile facts about the user.
- `agent_self_model`: key/value facts about the agent's self-model.
- `open_threads`: unresolved topics, questions, and active lines of thought.
- `tasks`: user-assigned or self-assigned goals.
- `tool_experiences`: records of significant tool use.
- `proactive_messages`: candidate initiative messages; Stage 1 does not send them.
- `personality_state`: durable emotional and motivational state.
- `relationship_state`: durable model of the relationship with the user.

## Obsidian Vault

The vault writer creates these folders:

- `00_Inbox`
- `01_Daily`
- `02_Episodes`
- `03_Beliefs`
- `04_User`
- `05_Self`
- `06_Projects`
- `07_OpenThreads`
- `08_Dreams`
- `09_ToolExperience`
- `10_Archive`

Each note uses YAML frontmatter with id, type, timestamps, importance, tags, status, and source event ids.

## Future Roadmap

Stage 2 can add real service adapters behind the existing interfaces:

1. Ollama-backed `LocalLLMClient`.
2. Claude-backed `DeepLLMClient` and routing.
3. Telegram bot polling/webhook gateway.
4. Real web search provider.
5. Playwright read-only browser actions.
6. Google OAuth and read-only Drive/Docs/Calendar/Gmail integrations.
7. Retrieval interfaces backed by embeddings/vector search.
8. More sophisticated belief revision, contradiction detection, and autobiographical consolidation.

The Stage 1 design keeps these extensions isolated behind interfaces so the durable personality substrate remains stable while cognition and tools improve.
