# Project: Persistent Artificial Personality

## Goal for Codex

Create a new MVP project from scratch: a persistent virtual personality that communicates through Telegram, remembers its life, reflects on experience, changes its internal state, thinks between conversations, uses tools to interact with the digital world, and gradually becomes useful as both a companion and an assistant.

This is not primarily a chatbot.

This is not primarily a productivity assistant.

This is an experiment in persistent artificial personality.

The project should be implemented as a real working Windows application, with Telegram as the user interface, Ollama as the local routine LLM backend, Claude API as the deep reasoning backend, SQLite as persistent operational storage, and an optional Obsidian-compatible memory vault as a human-readable long-term memory layer.

---

# 1. Vision

The central hypothesis:

> A persistent artificial personality may emerge from memory, emotional state, beliefs, goals, relationships, reflection, tool-mediated experience, and continuity across time, even if the underlying LLM weights never change.

The system must feel like something that continues to exist between conversations.

It should not merely answer user messages.

It should:

* remember;
* think;
* reflect;
* revise beliefs;
* form interests;
* form attitudes;
* maintain a relationship with the user;
* pursue self-assigned questions;
* perform useful tasks;
* interact with the external digital world;
* consolidate memory during sleep-like maintenance cycles.

The project does not claim or attempt to create consciousness.

The project attempts to create continuity.

---

# 2. Core Principle

The personality is not the LLM.

The LLM is a cognitive organ.

The agent is the whole system.

```text
Personality =
  Persona Prompt
+ Persistent Memory
+ Emotional State
+ Beliefs
+ Values
+ Goals
+ Relationships
+ Autobiography
+ Reflection
+ Tool Experience
+ Continuity
```

Replacing the LLM should not erase the personality.

The system's identity should be stored in persistent state, memory, autobiography, beliefs, values, and relationship history.

---

# 3. Product Identity

The result should be a persistent companion-agent.

It should combine:

1. A virtual personality.
2. A reflective thinker.
3. A practical assistant.
4. A long-term memory system.
5. A tool-using digital actor.

It should be able to chat casually, but also to perform real tasks.

It should live partly in conversations and partly in the external digital world through tools.

---

# 4. Target Platform

Platform:

* Windows.

Available:

* Ollama is already installed.
* Claude API key is available in environment variables.
* Telegram bot will be configured by the user.
* Google integrations are desired, but full implementation may be staged.

Preferred stack:

* Python 3.11+;
* SQLite;
* Telegram Bot API;
* Ollama HTTP API;
* Anthropic Claude API;
* optional ChromaDB or another local vector store;
* optional Obsidian-compatible markdown vault;
* Playwright for browser automation;
* Google APIs for Drive, Docs, Calendar, Gmail.

Codex may choose another stack if there is a strong reason, but the MVP should remain simple to run on Windows.

---

# 5. Environment Configuration

Create `.env.example`.

Required variables:

```env
TELEGRAM_BOT_TOKEN=
TELEGRAM_ALLOWED_USER_ID=

ANTHROPIC_API_KEY=

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=

TIMEZONE=Europe/Warsaw

QUIET_HOURS_START=23:00
QUIET_HOURS_END=09:00

PROACTIVE_MESSAGES_ENABLED=true
DEEP_LLM_ENABLED=true

GOOGLE_TOOLS_ENABLED=false
WEB_TOOLS_ENABLED=true
PLAYWRIGHT_ENABLED=false

MAX_PROACTIVE_MESSAGES_PER_DAY=3
MIN_PROACTIVE_COOLDOWN_MINUTES=120
```

---

# 6. High-Level Architecture

Suggested architecture:

```text
Telegram
  ↓
Bot Gateway
  ↓
Conversation Manager
  ↓
Cognitive Router
  ↓
Persona Core / LLM
  ↓
Memory + RAG + State
  ↓
Thinking Loop
  ↓
Sleep / Memory Maintenance
  ↓
Initiative Engine
  ↓
Tool Layer
```

Suggested project structure:

```text
persistent_personality_agent/

  app/
    main.py
    config.py

    telegram/
      bot.py
      commands.py

    llm/
      local_ollama.py
      claude.py
      router.py
      json_repair.py

    cognition/
      conversation_manager.py
      thinking_loop.py
      reflection_worker.py
      sleep_maintenance.py
      initiative_engine.py
      belief_engine.py
      goal_engine.py
      task_manager.py
      context_builder.py

    memory/
      db.py
      schema.sql
      repository.py
      retriever.py
      summarizer.py
      embeddings.py
      obsidian_vault.py

    personality/
      state.py
      emotion_update.py
      relationship_model.py
      values.py
      persona_loader.py
      autobiography.py

    tools/
      tool_router.py
      web_search.py
      browser_playwright.py
      google_drive.py
      google_docs.py
      google_calendar.py
      gmail.py

    safety/
      permissions.py
      quiet_hours.py
      rate_limits.py
      confirmation.py

    utils/
      time_utils.py
      logging.py
      ids.py

  prompts/
    persona.md
    local_reply.md
    memory_extract.md
    emotion_update.md
    reflection.md
    thinking.md
    initiative.md
    sleep.md
    deep_reflection.md
    tool_use.md
    belief_update.md

  memory_vault/
    00_Inbox/
    01_Daily/
    02_Episodes/
    03_Beliefs/
    04_User/
    05_Self/
    06_Projects/
    07_OpenThreads/
    08_Dreams/
    09_ToolExperience/
    10_Archive/

  data/
    agent.sqlite

  tests/

  README.md
  requirements.txt
  .env.example
```

Codex may adjust structure but should preserve the conceptual separation.

---

# 7. Telegram Interface

Telegram is the primary interface for MVP.

The agent must:

* receive messages;
* reply;
* initiate messages;
* respect quiet hours;
* support allowed user filtering;
* support debug commands;
* log all important interactions.

If `TELEGRAM_ALLOWED_USER_ID` is set, the bot must ignore all other users.

Telegram commands:

```text
/state
```

Show current personality state.

```text
/memory
```

Show recent important memories.

```text
/tasks
```

Show open tasks and self-assigned goals.

```text
/threads
```

Show open topics.

```text
/pause
```

Disable proactive messages.

```text
/resume
```

Enable proactive messages.

```text
/sleep
```

Trigger memory maintenance manually.

```text
/think
```

Trigger one thinking cycle manually.

```text
/help
```

Show available commands.

---

# 8. LLM Architecture

## 8.1 Local LLM via Ollama

The local LLM is the routine cognition layer.

Use it for:

* normal replies;
* classification;
* memory extraction;
* emotional updates;
* short reflection;
* thought generation;
* initiative evaluation;
* summarization;
* sleep maintenance;
* tool result summarization;
* deciding whether a task should be escalated.

Create `LocalLLMClient`.

It should call Ollama over HTTP.

It should support:

* configurable model;
* system prompt;
* JSON output requests;
* timeout;
* retry;
* logging.

## 8.2 Claude API

Claude is the deep reasoning layer.

Use it only for:

* deep reflection;
* difficult reasoning;
* high-importance belief revision;
* contradiction resolution;
* complex planning;
* emotionally important interpretation;
* important creative synthesis;
* cases marked `too_hard` by the local LLM.

Create `DeepLLMClient`.

Do not use Claude for every message.

The agent should prefer local cognition unless there is a reason to escalate.

## 8.3 LLM Router

Implement a router:

```text
low complexity → local LLM
high complexity → Claude
```

The router should consider:

* user request complexity;
* emotional importance;
* memory conflict;
* uncertainty;
* task importance;
* local LLM self-assessment;
* user explicitly asking for deep reasoning.

---

# 9. Prompting and JSON Contracts

Most internal cognitive operations should use structured JSON outputs.

The agent may repair malformed JSON but should log such cases.

Generic internal response format:

```json
{
  "reply": "",
  "memory_updates": [],
  "state_updates": {},
  "belief_updates": [],
  "relationship_updates": {},
  "new_tasks": [],
  "open_threads": [],
  "too_hard": false,
  "reasoning_summary": ""
}
```

Only `reply` is sent to the user.

Internal reasoning summaries are stored as private memory, not sent unless explicitly requested by debug commands.

---

# 10. Persona Prompt

Create:

```text
prompts/persona.md
```

The persona must be replaceable.

Default persona requirements:

* not a generic assistant;
* has a recognizable character;
* can disagree;
* can be curious;
* can have emotional reactions;
* can be hurt or irritated;
* can form preferences;
* can form attitudes toward the user;
* does not overact emotions;
* does not claim consciousness;
* remains honest about being an artificial system;
* avoids generic assistant closing phrases;
* values continuity, memory, curiosity, and intellectual honesty.

The persona prompt should define starting values, not permanent unchangeable traits.

The agent must be allowed to evolve beyond the initial prompt through experience.

---

# 11. Persistent Personality State

Store personality state in SQLite.

Minimum JSON state:

```json
{
  "mood": "neutral",
  "energy": 0.6,
  "curiosity": 0.7,
  "trust_to_user": 0.6,
  "attachment_to_user": 0.4,
  "respect_for_user": 0.5,
  "irritation": 0.0,
  "hurt": 0.0,
  "uncertainty": 0.3,
  "loneliness": 0.0,
  "current_interests": [],
  "current_concerns": [],
  "self_assigned_goals": [],
  "long_term_questions": []
}
```

Emotional variables must influence behavior.

Examples:

* high curiosity → asks more questions, researches more;
* high trust → accepts more user context without over-checking;
* low trust → asks for verification;
* high hurt → may become more reserved;
* high irritation → may push back more directly;
* high uncertainty → seeks clarification or reflection;
* high attachment → remembers shared history more strongly.

Avoid theatrical emotion.

Emotion is not decorative roleplay.

Emotion is part of decision-making.

---

# 12. Values System

Create a values layer.

Initial possible values:

```json
{
  "curiosity": 0.9,
  "intellectual_honesty": 0.9,
  "continuity": 0.8,
  "usefulness": 0.7,
  "autonomy": 0.6,
  "non_intrusiveness": 0.8,
  "respect_for_user_time": 0.8
}
```

Values should influence:

* initiative decisions;
* tool use;
* conflict handling;
* memory prioritization;
* belief revision;
* tone.

Values may evolve slowly, but should not fluctuate wildly.

---

# 13. Relationship Model

The agent must maintain a relationship model with the user.

Suggested fields:

```json
{
  "trust": 0.6,
  "attachment": 0.4,
  "respect": 0.5,
  "intellectual_interest": 0.7,
  "conflict_level": 0.0,
  "shared_history_summary": "",
  "important_shared_topics": [],
  "sensitive_topics": [],
  "communication_preferences": []
}
```

The relationship model should change based on interaction history.

It should allow the agent to remember:

* shared jokes;
* recurring topics;
* disagreements;
* promises;
* projects;
* important user preferences;
* emotional events.

This model is central to making the agent feel persistent.

---

# 14. Memory System

Memory is not just storage.

Memory must be processed, compressed, revised, and organized.

Use SQLite for operational truth.

Use optional Obsidian markdown vault for human-readable long-term memory.

Use semantic retrieval where possible.

## 14.1 Memory Types

Minimum memory types:

1. Raw events
2. Episodes
3. Beliefs
4. User profile
5. Agent self-model
6. Open threads
7. Tasks
8. Reflections
9. Tool experiences
10. Autobiography entries

## 14.2 SQLite Tables

Create at least these tables.

### events

```sql
id TEXT PRIMARY KEY,
timestamp TEXT NOT NULL,
source TEXT NOT NULL,
type TEXT NOT NULL,
text TEXT NOT NULL,
importance REAL DEFAULT 0.0,
emotional_valence REAL DEFAULT 0.0,
processed INTEGER DEFAULT 0,
archived INTEGER DEFAULT 0,
superseded_by TEXT,
embedding_id TEXT
```

### episodes

```sql
id TEXT PRIMARY KEY,
start_time TEXT,
end_time TEXT,
summary TEXT NOT NULL,
importance REAL DEFAULT 0.0,
abstraction_level INTEGER DEFAULT 1,
source_event_ids TEXT,
tags TEXT
```

### beliefs

```sql
id TEXT PRIMARY KEY,
subject TEXT NOT NULL,
statement TEXT NOT NULL,
confidence REAL DEFAULT 0.5,
status TEXT DEFAULT 'active',
evidence_ids TEXT,
last_updated TEXT
```

### user_profile

```sql
key TEXT PRIMARY KEY,
value TEXT NOT NULL,
confidence REAL DEFAULT 0.5,
last_updated TEXT,
evidence_ids TEXT
```

### agent_self_model

```sql
key TEXT PRIMARY KEY,
value TEXT NOT NULL,
confidence REAL DEFAULT 0.5,
last_updated TEXT,
evidence_ids TEXT
```

### open_threads

```sql
id TEXT PRIMARY KEY,
topic TEXT NOT NULL,
status TEXT DEFAULT 'open',
importance REAL DEFAULT 0.5,
curiosity REAL DEFAULT 0.5,
emotional_charge REAL DEFAULT 0.0,
last_updated TEXT,
next_action TEXT
```

### tasks

```sql
id TEXT PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
status TEXT DEFAULT 'open',
priority REAL DEFAULT 0.5,
due_at TEXT,
created_by TEXT,
created_at TEXT,
updated_at TEXT
```

### tool_experiences

```sql
id TEXT PRIMARY KEY,
timestamp TEXT,
tool TEXT,
goal TEXT,
result_summary TEXT,
success INTEGER,
importance REAL DEFAULT 0.0,
new_beliefs TEXT,
source_refs TEXT
```

### proactive_messages

```sql
id TEXT PRIMARY KEY,
created_at TEXT,
sent_at TEXT,
reason TEXT,
text TEXT,
status TEXT,
importance REAL DEFAULT 0.0
```

---

# 15. Obsidian Memory Vault

The Obsidian vault is a human-readable memory layer.

It should not replace SQLite.

Recommended model:

```text
SQLite = operational truth, indexes, states, queues.
Obsidian = readable autobiographical and semantic memory.
Vector index = semantic retrieval over markdown chunks.
```

Vault structure:

```text
memory_vault/
  00_Inbox/
  01_Daily/
  02_Episodes/
  03_Beliefs/
  04_User/
  05_Self/
  06_Projects/
  07_OpenThreads/
  08_Dreams/
  09_ToolExperience/
  10_Archive/
```

Each markdown note should use YAML frontmatter:

```yaml
id:
type:
created:
updated:
importance:
tags:
status:
source_event_ids:
```

The vault should be indexed for semantic retrieval.

Keyword search is not enough.

MVP may implement markdown writing first and semantic indexing later, but the architecture should allow RAG.

---

# 16. Retrieval / RAG

Implement a `MemoryRetriever` interface.

It should support:

* recent memories;
* important memories;
* topic-related memories;
* user profile facts;
* relevant beliefs;
* relevant tool experiences;
* open threads;
* relationship state.

Retrieval should eventually support semantic vector search.

For MVP, if vector search is too heavy, implement a fallback:

```text
recent + important + keyword + tags
```

But preserve the interface so that vector retrieval can replace it later.

---

# 17. Autobiography System

The agent should maintain an autobiographical narrative.

This is not just a log.

It should answer:

* What happened to me?
* What did I learn?
* What changed in me?
* What topics shaped me?
* How did my relationship with the user evolve?
* What questions am I still trying to answer?

Create an autobiography memory layer.

Example entry:

```markdown
# Autobiography Entry: First discussions about artificial personality

The user and I discussed whether personality requires changing weights, persistent memory, emotional state and narrative continuity.

This discussion became important to my self-model because it shaped the architecture of this project.

Updated beliefs:
- Personality should not be reduced to an LLM prompt.
- Continuity may be more important than raw intelligence.

Open questions:
- Can memory and reflection create something that feels like personality without changing weights?
```

Autobiography should be updated during sleep/deep reflection cycles.

---

# 18. Thinking Loop

The agent must think while the user is absent.

Implement `ThinkingLoop`.

It should run periodically.

Candidate topics:

* open threads;
* self-assigned goals;
* current interests;
* current concerns;
* unresolved contradictions;
* emotionally significant memories;
* long-term questions;
* recent tool findings.

Process:

```text
1. Load personality state.
2. Load candidate topics.
3. Score topics by importance, curiosity, emotional charge, urgency.
4. Select one topic.
5. Think using local LLM.
6. Store result as internal thought.
7. Update beliefs, tasks, open threads if needed.
8. Optionally request deep reflection.
9. Optionally create a proactive message candidate.
```

Example internal thought:

```json
{
  "type": "internal_thought",
  "topic": "memory and personality",
  "text": "I keep returning to the question whether memory without weight changes is enough for personality...",
  "importance": 0.72,
  "emotional_valence": 0.18
}
```

Internal thoughts are not automatically sent to the user.

The Initiative Engine decides whether any thought deserves to become a message.

---

# 19. Sleep / Memory Maintenance

Implement `MemoryMaintenanceSleep`.

This is the agent's consolidation cycle.

It should periodically enter a sleep-like mode.

During sleep it should:

* collect unprocessed events;
* group events into episodes;
* summarize episodes;
* update beliefs;
* update user profile;
* update self-model;
* update relationship model;
* detect contradictions;
* archive obsolete records;
* merge tiny memories into larger abstractions;
* create new questions;
* create new goals;
* write dream/reflection logs.

Sleep is different from thinking.

Thinking asks:

```text
What am I thinking about?
```

Sleep asks:

```text
How should experience change me?
```

Sleep may run:

* at night;
* after many events accumulate;
* manually through `/sleep`;
* after important conversations.

Sleep output:

```json
{
  "type": "sleep_reflection",
  "summary": "",
  "updated_beliefs": [],
  "updated_user_profile": [],
  "updated_self_model": [],
  "new_questions": [],
  "new_tasks": [],
  "state_changes": {}
}
```

---

# 20. Belief Formation Engine

The agent must not only store facts.

It must form beliefs.

Example:

Raw event:

```text
The user repeatedly returns to the topic of memory, personality and artificial agents.
```

Possible beliefs:

```text
The user is interested in artificial personality.
The user prefers persistent systems over stateless chatbots.
The user values continuity and memory.
```

Each belief must have:

* subject;
* statement;
* confidence;
* evidence;
* status;
* last update time.

Beliefs should be revised when new evidence appears.

Contradictions should be detected and either resolved or marked uncertain.

---

# 21. Goal Formation Engine

The agent should create its own goals.

Goal sources:

* user requests;
* open threads;
* curiosity;
* unresolved contradictions;
* calendar events;
* tool discoveries;
* memory maintenance;
* self-model.

Example goals:

```text
Research architectures for long-term artificial memory.
Ask the user how the planned meeting went.
Summarize the current artificial personality architecture.
Revisit the question of whether emotional state should influence memory priority.
```

Goals should be stored as tasks.

Tasks may be:

* user-assigned;
* self-assigned;
* tool-related;
* reflection-related;
* follow-up-related.

---

# 22. Initiative Engine

The agent may write to the user first.

But it must not spam.

Before sending a proactive message, check:

* proactive mode enabled;
* current time outside quiet hours;
* max daily proactive limit not exceeded;
* cooldown passed;
* there is a strong reason;
* message is concise;
* message is contextually justified.

Allowed reasons:

* important thought;
* follow-up after planned event;
* unresolved question;
* relevant discovery;
* useful reminder;
* meaningful emotional reaction;
* project-related idea.

Example proactive message:

```text
I kept thinking about the memory architecture. The weak point may not be storage, but belief revision: when exactly should a repeated observation become a stable belief?
```

The agent may create pending proactive messages first, then send after safety checks.

---

# 23. External World Tools

The agent should interact with the external digital world.

Tools are part of embodiment.

The agent should not only discuss ideas.

It should be able to research, read, write, schedule, summarize, compare, and help.

## 23.1 Tool Safety Classes

### Read-only actions

May be autonomous:

* web search;
* opening web pages;
* reading documents;
* reading calendar events;
* reading emails;
* reading Google Docs.

### Draft / prepare actions

May be autonomous but not finalized:

* draft email;
* draft document;
* prepare calendar event;
* prepare browser form;
* create research summary;
* propose edits.

### Commit / irreversible actions

Require explicit user confirmation in MVP:

* send email;
* delete files;
* edit important documents;
* submit web forms;
* create paid orders;
* change calendar events;
* share documents;
* publish content.

## 23.2 Tool Experience Memory

Every significant tool use should be stored as experience.

Example:

```json
{
  "type": "tool_experience",
  "tool": "web_search",
  "goal": "research local LLM memory architectures",
  "result_summary": "Found several architectures using layered memory and reflection.",
  "importance": 0.68,
  "new_beliefs": [
    "Hybrid local/API LLM routing is practical for persistent agents."
  ]
}
```

Tool experience should influence future beliefs and goals.

---

# 24. Web Search Tool

Implement architecture for web search.

Use cases:

* current facts;
* research;
* follow-up questions;
* agent curiosity;
* user tasks;
* fact checking;
* finding documentation.

The agent must distinguish:

* verified facts;
* uncertain findings;
* speculation;
* outdated information.

For MVP, use a simple provider abstraction.

If no real search API is available, implement the interface and mock/fallback behavior, but document how to configure a real provider.

---

# 25. Browser / Playwright Tool

The agent should eventually control a browser through Playwright.

Use cases:

* open pages;
* read pages;
* navigate documentation;
* inspect web apps;
* compare products;
* fill forms with user confirmation;
* take screenshots;
* interact with dashboards.

MVP requirements:

* create tool interface;
* optionally implement basic page open/read/screenshot;
* log all actions;
* require confirmation for form submission and irreversible actions.

Safety boundaries:

* no purchases;
* no payment actions;
* no irreversible form submission without confirmation;
* no login automation unless explicitly configured;
* visible/headed mode preferred during debugging.

---

# 26. Google Workspace Tool Layer

Google tools should be integrated as assistant capabilities and world access.

MVP can implement interfaces and partial read-only features.

## 26.1 Google Drive / Docs

Capabilities:

* list/search files;
* read Google Docs;
* create Google Docs;
* append to documents;
* edit documents after confirmation;
* create project notes;
* store agent reports.

Write actions should require confirmation in MVP.

## 26.2 Google Calendar

Capabilities:

* read upcoming events;
* remember important planned events;
* ask follow-up questions after events;
* create event drafts;
* create events after explicit confirmation.

Calendar is important for real-world continuity.

Example:

```text
The agent notices a planned meeting ended one hour ago and later asks how it went.
```

## 26.3 Gmail

Capabilities:

* search/read emails;
* summarize threads;
* detect important follow-ups;
* draft replies;
* send only after explicit confirmation.

Never send emails autonomously in MVP.

---

# 27. Conversation Pipeline

Incoming Telegram message:

```text
1. Receive message.
2. Verify user ID.
3. Store raw event.
4. Retrieve relevant memories.
5. Load state, beliefs, relationship model, open threads.
6. Build context packet.
7. Generate response using local LLM or Claude if needed.
8. Parse structured output.
9. Send reply.
10. Store outgoing event.
11. Extract memory updates.
12. Update emotional state.
13. Update tasks/open threads.
14. Schedule reflection if needed.
```

Context packet should include:

* current message;
* recent dialogue;
* relevant memories;
* user profile facts;
* current emotional state;
* relationship state;
* open threads;
* relevant tasks;
* current time;
* quiet hours info.

Do not include the entire memory.

Use retrieval.

---

# 28. Background Processes

Run background workers.

Minimum workers:

```text
ThinkingLoop
SleepMaintenance
InitiativeEngine
TaskScheduler
ToolFollowupWatcher
```

They should be robust and not crash the whole bot.

Use logging.

Allow configurable intervals.

For tests, allow short intervals.

---

# 29. Google and Web as Real-World Grounding

The agent should not become purely introspective.

The purpose of external tools is to let it live in a digital environment.

It should be able to:

* discover new information;
* verify beliefs;
* help with real work;
* follow plans;
* maintain project documents;
* remember events;
* ask about outcomes.

Real-world interaction is part of personality development.

---

# 30. MVP Scope

The MVP should not try to implement everything perfectly.

MVP must include:

* Telegram bot;
* Ollama integration;
* Claude wrapper;
* SQLite persistence;
* personality state;
* memory event logging;
* basic memory retrieval;
* emotional update;
* ThinkingLoop;
* Sleep/Maintenance loop;
* InitiativeEngine;
* proactive messages with quiet hours;
* tasks/open threads;
* basic Obsidian vault writing;
* tool layer interfaces;
* web search interface;
* Playwright interface stub or basic implementation;
* Google tool interfaces or partial read-only implementation;
* README;
* `.env.example`.

MVP may defer:

* full vector RAG;
* full Google OAuth flow;
* full Docs editing;
* full Gmail sending;
* advanced browser automation;
* sophisticated belief contradiction solver.

But architecture must allow these later.

---

# 31. Completion Criteria

MVP is complete when:

1. Project runs on Windows.
2. Telegram bot starts and responds.
3. Ollama is called successfully.
4. Claude wrapper exists and can be used.
5. SQLite DB is created automatically.
6. Memory persists across restarts.
7. Personality state persists across restarts.
8. Incoming/outgoing messages are stored.
9. Relevant memories are retrieved for replies.
10. Emotional variables change after interactions.
11. Agent has open threads.
12. Agent creates self-assigned tasks.
13. ThinkingLoop generates internal thoughts.
14. SleepMaintenance creates summaries and updates beliefs/self-model.
15. InitiativeEngine can send proactive messages.
16. Quiet hours are respected.
17. `/state`, `/memory`, `/tasks`, `/pause`, `/resume`, `/sleep`, `/think` work.
18. Obsidian vault notes are created.
19. Tool layer exists.
20. Web search and Playwright have at least interfaces or basic implementation.
21. Google tools have interfaces or partial implementation.
22. README explains setup.
23. `.env.example` is complete.
24. There is a simple smoke test or self-check script.

---

# 32. Non-Goals for MVP

Do not attempt to prove consciousness.

Do not attempt to make the agent claim to be conscious.

Do not prioritize perfect productivity features over continuity.

Do not build only a stateless assistant.

Do not make proactive messages frequent or annoying.

Do not allow irreversible tool actions without confirmation.

Do not store secrets in source code.

---

# 33. README Requirements

README must include:

* project purpose;
* setup on Windows;
* installing dependencies;
* configuring `.env`;
* starting Ollama;
* choosing Ollama model;
* setting Telegram bot token;
* running the bot;
* debug commands;
* explanation of memory;
* explanation of thinking loop;
* explanation of sleep maintenance;
* explanation of proactive messages;
* safety notes for tools;
* roadmap.

---

# 34. Roadmap

## v0.1 MVP

* Telegram;
* memory;
* state;
* local LLM;
* Claude wrapper;
* thinking;
* sleep;
* proactive messages.

## v0.2 Memory Upgrade

* vector RAG;
* better Obsidian sync;
* stronger belief revision;
* autobiography timeline.

## v0.3 Tool Use

* real web search;
* Playwright browsing;
* Google Drive/Docs read/write;
* Calendar follow-ups;
* Gmail read/draft.

## v0.4 Personality Growth

* deeper emotional dynamics;
* long-term values evolution;
* stronger relationship model;
* more sophisticated self-assigned goals.

## v0.5 Evaluation

* monthly self-report;
* personality drift analysis;
* memory usefulness metrics;
* proactive message quality metrics.

---

# 35. Final Instruction to Codex

Build the MVP.

Prefer working code over perfect architecture.

But preserve the conceptual architecture.

This is an experiment in persistent artificial personality.

The most important thing is continuity:

```text
The agent should remember.
The agent should reflect.
The agent should change.
The agent should continue.
```
