from typing import List, Dict
from datetime import datetime

class ConversationMemory:
    def __init__(self, max_messages: int = 10):
        self.messages = []
        self.max_messages = max_messages
        
    def add_message(self, role: str, content: str):
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        }
        self.messages.append(message)
        # Keep only the last `max_messages` messages
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]
            
    def get_conversation_history(self) -> List[Dict]:
        return self.messages.copy()

    def clear_memory(self):
        self.messages = []