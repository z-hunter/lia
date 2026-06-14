from __future__ import annotations
import json
class LocalLLMClient:
    def generate(self,prompt:str)->str: raise NotImplementedError
    def generate_json(self,prompt:str)->dict: raise NotImplementedError
class DeepLLMClient(LocalLLMClient): pass
class MockLocalLLMClient(LocalLLMClient):
    def generate(self,prompt:str)->str: return "Mock thought: I am connecting recent memory with my continuing goals."
    def generate_json(self,prompt:str)->dict: return {"text":self.generate(prompt),"importance":0.6,"task":"Revisit this thread after more evidence."}
class MockDeepLLMClient(DeepLLMClient):
    def generate(self,prompt:str)->str: return "Mock deep reflection: continuity is represented by persisted state, not by a single prompt."
    def generate_json(self,prompt:str)->dict: return {"reflection":self.generate(prompt),"new_beliefs":[]}
