CREATE TABLE IF NOT EXISTS events (
  id TEXT PRIMARY KEY, timestamp TEXT NOT NULL, source TEXT NOT NULL, type TEXT NOT NULL,
  text TEXT NOT NULL, importance REAL DEFAULT 0.0, emotional_valence REAL DEFAULT 0.0,
  processed INTEGER DEFAULT 0, archived INTEGER DEFAULT 0, superseded_by TEXT, embedding_id TEXT
);
CREATE TABLE IF NOT EXISTS episodes (
  id TEXT PRIMARY KEY, start_time TEXT, end_time TEXT, summary TEXT NOT NULL,
  importance REAL DEFAULT 0.0, abstraction_level INTEGER DEFAULT 1, source_event_ids TEXT, tags TEXT
);
CREATE TABLE IF NOT EXISTS beliefs (
  id TEXT PRIMARY KEY, subject TEXT NOT NULL, statement TEXT NOT NULL, confidence REAL DEFAULT 0.5,
  status TEXT DEFAULT 'active' CHECK(status IN ('active','uncertain','superseded')),
  evidence_ids TEXT, last_updated TEXT
);
CREATE TABLE IF NOT EXISTS user_profile (
  key TEXT PRIMARY KEY, value TEXT NOT NULL, confidence REAL DEFAULT 0.5, last_updated TEXT, evidence_ids TEXT
);
CREATE TABLE IF NOT EXISTS agent_self_model (
  key TEXT PRIMARY KEY, value TEXT NOT NULL, confidence REAL DEFAULT 0.5, last_updated TEXT, evidence_ids TEXT
);
CREATE TABLE IF NOT EXISTS open_threads (
  id TEXT PRIMARY KEY, topic TEXT NOT NULL, status TEXT DEFAULT 'open', importance REAL DEFAULT 0.5,
  curiosity REAL DEFAULT 0.5, emotional_charge REAL DEFAULT 0.0, last_updated TEXT, next_action TEXT
);
CREATE TABLE IF NOT EXISTS tasks (
  id TEXT PRIMARY KEY, title TEXT NOT NULL, description TEXT, status TEXT DEFAULT 'open', priority REAL DEFAULT 0.5,
  due_at TEXT, created_by TEXT, created_at TEXT, updated_at TEXT
);
CREATE TABLE IF NOT EXISTS tool_experiences (
  id TEXT PRIMARY KEY, timestamp TEXT, tool TEXT, goal TEXT, result_summary TEXT, success INTEGER,
  importance REAL DEFAULT 0.0, new_beliefs TEXT, source_refs TEXT
);
CREATE TABLE IF NOT EXISTS proactive_messages (
  id TEXT PRIMARY KEY, created_at TEXT, sent_at TEXT, reason TEXT, text TEXT, status TEXT, importance REAL DEFAULT 0.0
);
CREATE TABLE IF NOT EXISTS personality_state (key TEXT PRIMARY KEY, value TEXT NOT NULL, updated_at TEXT);
CREATE TABLE IF NOT EXISTS relationship_state (key TEXT PRIMARY KEY, value TEXT NOT NULL, updated_at TEXT);
