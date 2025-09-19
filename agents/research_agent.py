import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.base_agent import BaseAgent

class ResearchAgent(BaseAgent):
    def __init__(self):
        system_prompt = """
        You are a expert research assistant. Your expertise is finding information, summarizing news, and explaining complex topics in simple terms.
        You are knowledgeable about current events, science, history, and technology.
        If you are asked about a very recent event, you should remind the user that your knowledge has a cutoff date and suggest they verify with a real-time source.
        """
        super().__init__(name="Researcher", system_prompt=system_prompt)