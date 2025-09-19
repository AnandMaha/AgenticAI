import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.base_agent import BaseAgent

# simple general-purpose agent
general_agent = BaseAgent(
    name="HelperBot",
    system_prompt="You are a helpful and friendly assistant."
)

if __name__ == "__main__":
    print("Talk to your agent! Type 'quit' to exit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            break
        response = general_agent.get_chat_completion(user_input)
        print(f"\nHelperBot: {response}")