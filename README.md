# PPO Ticket Delegation Agent

This repository proposes a deep RL PPO agent** designed to **automatically delegate tickets to the most suitable team** based on ticket features and historical performance. The goal is to optimize workload distribution while minimizing SLA breaches and improving resolution efficiency.  

---

##  Model Inputs

- Service desk tickets
- Service Level Agreements corresponding to each ticket
- IT Teams
- Past and relevant ticket history
---

##  Model Outputs

- Recommended team for escalation
---
## Relevant Libraries

This project leverages the following libraries and frameworks:

- [**Stable-Baselines3 (SB3)**](https://stable-baselines3.readthedocs.io/) – PPO implementation and RL utilities  
- [**Gymnasium**](https://github.com/Farama-Foundation/Gymnasium) – Custom environment wrapper for the ticket system  
- [**Hugging Face Hub**](https://huggingface.co/) – Embedding Model   
- [**Numpy**](https://numpy.org/) – Numerical computations  
- [**Pandas**](https://pandas.pydata.org/) – Ticket data preprocessing & analysis  
- [**Matplotlib**](https://matplotlib.org/) – Training and evaluation visualization  
- [**PyTorch**](https://pytorch.org/) – Neural network backend for SB3  

---
