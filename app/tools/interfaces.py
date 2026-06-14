from __future__ import annotations
class Tool:
    name="tool"
    def run(self, *args, **kwargs): raise NotImplementedError
class MockTool(Tool):
    def run(self,*args,**kwargs): return {"success":True,"tool":self.name,"summary":"mock result","args":args,"kwargs":kwargs}
class WebSearchTool(MockTool): name="web_search"
class PlaywrightTool(MockTool): name="playwright"
class GoogleDriveTool(MockTool): name="google_drive"
class GoogleDocsTool(MockTool): name="google_docs"
class GoogleCalendarTool(MockTool): name="google_calendar"
class GmailTool(MockTool): name="gmail"
