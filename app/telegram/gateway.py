from __future__ import annotations
class TelegramGateway:
    def send_message(self, chat_id:str, text:str)->None: raise NotImplementedError
class MockTelegramGateway(TelegramGateway):
    def send_message(self, chat_id:str, text:str)->None: print(f"[mock telegram] -> {chat_id}: {text}")
