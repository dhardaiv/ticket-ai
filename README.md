# PPO Ticket Delegation Agent 🎫🤖

> **Status:** 🚧 *This project is still in progress*  

This repository contains a **Proximal Policy Optimization (PPO) agent** designed to **automatically delegate tickets to the most suitable team** based on ticket features and historical performance. The goal is to optimize workload distribution while minimizing SLA breaches and improving resolution efficiency.  

---

## 🚀 Features

- **Custom Gymnasium Environment** – Simulates a ticketing system with teams, tickets, priorities, and SLA rules.  
- **PPO Agent (Stable-Baselines3)** – Reinforcement learning agent that learns optimal delegation policies.  
- **Reward Function** – Configurable design to balance between SLA compliance, resolution efficiency, and fairness across teams.  
- **Flexible Inputs** – Accepts structured ticket data (e.g., features like priority, type, category).  
- **Logging & Evaluation** – Training logs, performance metrics, and model checkpoints included.  

---

## 📚 Libraries & Tools

This project leverages the following libraries and frameworks:

- [**Stable-Baselines3 (SB3)**](https://stable-baselines3.readthedocs.io/) – PPO implementation and RL utilities  
- [**Gymnasium**](https://github.com/Farama-Foundation/Gymnasium) – Custom environment wrapper for the ticket system  
- [**Hugging Face Hub**](https://huggingface.co/) – Embedding Model   
- [**Numpy**](https://numpy.org/) – Numerical computations  
- [**Pandas**](https://pandas.pydata.org/) – Ticket data preprocessing & analysis  
- [**Matplotlib**](https://matplotlib.org/) – Training and evaluation visualization  
- [**PyTorch**](https://pytorch.org/) – Neural network backend for SB3  

---
