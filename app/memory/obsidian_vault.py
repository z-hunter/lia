from __future__ import annotations
from pathlib import Path
from app.config import settings
from app.utils.time_utils import utc_now_iso

FOLDERS=["00_Inbox","01_Daily","02_Episodes","03_Beliefs","04_User","05_Self","06_Projects","07_OpenThreads","08_Dreams","09_ToolExperience","10_Archive"]
class ObsidianVaultWriter:
    def __init__(self, root:Path|None=None): self.root=root or settings.vault_path; self.ensure()
    def ensure(self):
        for f in FOLDERS: (self.root/f).mkdir(parents=True, exist_ok=True)
    def write_note(self, folder:str, note_id:str, title:str, body:str, type:str="note", importance:float=.5, tags:list[str]|None=None, status:str="active", source_event_ids:list[str]|None=None)->Path:
        now=utc_now_iso(); safe="".join(c if c.isalnum() or c in "-_" else "_" for c in title)[:60]
        path=self.root/folder/f"{now[:10]}_{safe}_{note_id}.md"
        front="---\n"+f"id: {note_id}\ntype: {type}\ncreated: {now}\nupdated: {now}\nimportance: {importance}\ntags: {tags or []}\nstatus: {status}\nsource_event_ids: {source_event_ids or []}\n---\n\n"
        path.write_text(front+f"# {title}\n\n{body}\n", encoding="utf-8"); return path
