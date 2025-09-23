import numpy as np
from stable_baselines3 import PPO
from src.envs.ticket_assignment_env import TicketAssignmentEnv

team_perf = [
    {"IT Cloud Operations": 0.3},
    {"IT Enterprise Application Services": 0.2},
    {"IT End User Compute":0.4},
    {"IT Level 2 Service Desk": 0.5},
    {"IT Information Security": 0.1},
    {"IT Infrastructure Operations":0.4},
    {"IT Networks, Security Operations, Telecom": 0.6},
    {"IT Web Application Support":0.5}
]

team_to_idx = {team: i for i, team in enumerate(team_perf.keys())}
idx_to_team = {i: t for t, i in team_to_idx.items()}

# Load PPO model
ppo_model = PPO.load("models/ppo_ticket_agent")

def assign_team(ticket_features: np.ndarray) -> str:
    action, _ = ppo_model.predict(ticket_features, deterministic=True)
    return idx_to_team[action]
