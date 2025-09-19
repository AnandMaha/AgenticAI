from openai import OpenAI
from memory.conversation_memory import ConversationMemory
import os
from dotenv import load_dotenv

load_dotenv()  # Load the API key from .env

class BaseAgent:
    def __init__(self, name: str, system_prompt: str):
        self.name = name
        self.system_prompt = system_prompt
        self.memory = ConversationMemory()
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
    def get_chat_completion(self, user_query: str) -> str:
        """Sends the conversation history to OpenAI and gets a response."""
        # Prepare the messages: system prompt first, then conversation history, then the new user query
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(self.memory.get_conversation_history())
        messages.append({"role": "user", "content": user_query})
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7
            )
            ai_response = response.choices[0].message.content
            
            # Add this exchange to memory
            self.memory.add_message("user", user_query)
            self.memory.add_message("assistant", ai_response)
            
            return ai_response
            
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"