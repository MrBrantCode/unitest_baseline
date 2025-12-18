"""
QUESTION:
Implement a function `update_q_values_batch(q_values, obs, actions, rewards, gamma)` that updates a batch of Q-values using the Bellman equation in reinforcement learning. The function takes as input a 2D NumPy array `q_values` representing the current Q-values for different state-action pairs, a list of observed states `obs`, a list of actions taken in each observed state `actions`, a list of rewards received for each action taken `rewards`, and the discount factor for future rewards `gamma`. The function should update the Q-values batch based on the observed transitions and return the updated Q-values batch. Assume the learning rate `alpha` is 1.
"""

import numpy as np

def update_q_values_batch(q_values, obs, actions, rewards, gamma):
    for i in range(len(obs)):
        s = obs[i]
        a = actions[i]
        r = rewards[i]
        s_next = obs[i + 1] if i < len(obs) - 1 else None

        if s_next is not None:
            max_q_next = np.max(q_values[s_next])
        else:
            max_q_next = 0  # Q-value for terminal state is 0

        q_values[s, a] += 1 * (r + gamma * max_q_next - q_values[s, a])

    return q_values