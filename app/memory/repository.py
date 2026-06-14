from __future__ import annotations
import json, sqlite3
from typing import Any
from app.utils.ids import new_id
from app.utils.time_utils import utc_now_iso

class MemoryRepository:
    def __init__(self, conn: sqlite3.Connection): self.conn = conn
    def add_event(self, source: str, type: str, text: str, importance: float=0.0, emotional_valence: float=0.0, processed: bool=False) -> str:
        eid = new_id("evt"); ts = utc_now_iso()
        self.conn.execute("INSERT INTO events(id,timestamp,source,type,text,importance,emotional_valence,processed) VALUES(?,?,?,?,?,?,?,?)", (eid,ts,source,type,text,importance,emotional_valence,int(processed)))
        self.conn.commit(); return eid
    def unprocessed_events(self) -> list[sqlite3.Row]:
        return self.conn.execute("SELECT * FROM events WHERE processed=0 AND archived=0 ORDER BY timestamp").fetchall()
    def recent_events(self, limit:int=10, type: str|None=None) -> list[sqlite3.Row]:
        if type: return self.conn.execute("SELECT * FROM events WHERE type=? ORDER BY timestamp DESC LIMIT ?",(type,limit)).fetchall()
        return self.conn.execute("SELECT * FROM events ORDER BY timestamp DESC LIMIT ?",(limit,)).fetchall()
    def mark_events_processed(self, ids:list[str]) -> None:
        self.conn.executemany("UPDATE events SET processed=1 WHERE id=?", [(i,) for i in ids]); self.conn.commit()
    def create_episode(self, summary:str, event_ids:list[str], importance:float=.5, tags:list[str]|None=None) -> str:
        eid = new_id("epi"); now=utc_now_iso(); payload=json.dumps(event_ids); tag=json.dumps(tags or [])
        self.conn.execute("INSERT INTO episodes(id,start_time,end_time,summary,importance,source_event_ids,tags) VALUES(?,?,?,?,?,?,?)",(eid,now,now,summary,importance,payload,tag)); self.conn.commit(); return eid
    def upsert_belief(self, subject:str, statement:str, confidence:float=.5, evidence:list[str]|None=None, status:str="active") -> str:
        bid=new_id("bel"); now=utc_now_iso()
        self.conn.execute("INSERT INTO beliefs(id,subject,statement,confidence,status,evidence_ids,last_updated) VALUES(?,?,?,?,?,?,?)",(bid,subject,statement,confidence,status,json.dumps(evidence or []),now)); self.conn.commit(); return bid
    def list_beliefs(self, status:str|None="active") -> list[sqlite3.Row]:
        if status: return self.conn.execute("SELECT * FROM beliefs WHERE status=? ORDER BY last_updated DESC",(status,)).fetchall()
        return self.conn.execute("SELECT * FROM beliefs ORDER BY last_updated DESC").fetchall()
    def upsert_thread(self, topic:str, importance:float=.5, curiosity:float=.5, emotional_charge:float=0, next_action:str|None=None) -> str:
        tid=new_id("thr"); now=utc_now_iso()
        self.conn.execute("INSERT INTO open_threads(id,topic,importance,curiosity,emotional_charge,last_updated,next_action) VALUES(?,?,?,?,?,?,?)",(tid,topic,importance,curiosity,emotional_charge,now,next_action)); self.conn.commit(); return tid
    def open_threads(self) -> list[sqlite3.Row]: return self.conn.execute("SELECT * FROM open_threads WHERE status='open' ORDER BY (importance+curiosity+ABS(emotional_charge)) DESC").fetchall()
    def add_task(self,title:str,description:str="",created_by:str="agent",priority:float=.5) -> str:
        tid=new_id("tsk"); now=utc_now_iso(); self.conn.execute("INSERT INTO tasks(id,title,description,created_by,priority,created_at,updated_at) VALUES(?,?,?,?,?,?,?)",(tid,title,description,created_by,priority,now,now)); self.conn.commit(); return tid
    def add_proactive(self, reason:str, text:str, importance:float=.5, status:str="candidate") -> str:
        pid=new_id("pro"); self.conn.execute("INSERT INTO proactive_messages(id,created_at,reason,text,status,importance) VALUES(?,?,?,?,?,?)",(pid,utc_now_iso(),reason,text,status,importance)); self.conn.commit(); return pid
    def recent_proactive(self, limit:int=10): return self.conn.execute("SELECT * FROM proactive_messages ORDER BY created_at DESC LIMIT ?",(limit,)).fetchall()
    def get_kv(self, table:str, key:str) -> Any|None:
        row=self.conn.execute(f"SELECT value FROM {table} WHERE key=?",(key,)).fetchone(); return json.loads(row[0]) if row else None
    def set_kv(self, table:str, key:str, value:Any) -> None:
        self.conn.execute(f"INSERT INTO {table}(key,value,updated_at) VALUES(?,?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at",(key,json.dumps(value),utc_now_iso())); self.conn.commit()
