import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.base_agent import BaseAgent
from agents.orchestrator_agent import OrchestratorAgent
from agents.research_agent import ResearchAgent
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Initialize our agents
general_agent = BaseAgent("HelperBot", "You are a helpful and friendly assistant.")
research_agent = ResearchAgent()

# Create a dictionary of our specialized agents for the orchestrator
specialized_agents = {
    "researcher": research_agent,
    # We will add "coder" later
}

orchestrator = OrchestratorAgent(specialized_agents)

@app.route('/')
def home():
    return "Multi-Agent System is running! Send a POST request to /chat with a 'message'."

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    print(f"User asked: {user_message}")

    # Step 1: Let the orchestrator decide who handles this
    agent_key = orchestrator.route_query(user_message)

    # Step 2: Route the query to the chosen agent
    if agent_key == "general":
        final_response = general_agent.get_chat_completion(user_message)
    else:
        chosen_agent = specialized_agents[agent_key]
        final_response = chosen_agent.get_chat_completion(user_message)

    # Step 3: Return the response
    return jsonify({"response": final_response, "handled_by": agent_key})

if __name__ == '__main__':
    app.run(debug=True)