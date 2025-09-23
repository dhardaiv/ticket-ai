from llm_router import classify_ticket
from rl_router import assign_team
import numpy as np

def route_ticket(ticket: str, features: np.ndarray):
    category = classify_ticket(ticket)
    team = assign_team(features)
    return category, team

if __name__ == "__main__":
    ticket = "User cannot connect to VPN and gets repeated authentication failures."
    sample_features = np.random.randn(10).astype(np.float32)  # placeholder

    category, team = route_ticket(ticket, sample_features)

    print(f"Ticket: {ticket}")
    print(f"Category (LLM): {category}")
    print(f"Assigned Team (PPO): {team}")
