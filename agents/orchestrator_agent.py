import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from agents.base_agent import BaseAgent

class OrchestratorAgent(BaseAgent):
    def __init__(self, specialized_agents: dict = None):
        # A powerful system prompt that defines its role
        system_prompt = """
        You are an orchestrator. Your job is to analyze the user's request and decide if it's a general question or if it requires a specialized agent.
        You have these specialized agents at your disposal:
        - 'researcher': For questions about current events, news, or researching topics. Use for questions containing words like: research, news, latest, current, what's happening, update on.
        - 'coder': For questions about programming, code, scripts, algorithms. Use for questions containing words like: code, script, python, function, program, algorithm, debug.

        If the user's request clearly fits one of these specialties, respond with ONLY the keyword of that agent, like this: `researcher` or `coder`.
        If it's a general conversation, greeting, or doesn't fit a specialty, respond with ONLY the word `general`.
        """
        super().__init__(name="Orchestrator", system_prompt=system_prompt)
        self.specialized_agents = specialized_agents or {}

    def route_query(self, user_query: str) -> str:
        """Decides which agent should handle the query."""
        # Use the OpenAI API to decide (as defined in its system prompt)
        decision = self.get_chat_completion(user_query)
        decision = decision.strip().lower()

        # Check if the decision is one of our agent keywords
        if decision in self.specialized_agents:
            print(f"Orchestrator: Routing this to the {decision}.")
            return decision
        else:
            print("Orchestrator: Handling this as a general query myself.")
            return "general"