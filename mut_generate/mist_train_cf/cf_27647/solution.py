"""
QUESTION:
Implement the `reinforce_var_bound` function to calculate the variance bound for a reinforcement learning estimator. The function should take three parameters: `max_rew` (maximum reward), `disc` (discount factor), and `kappa` (a constant derived from Gaussian smoothing), and return the variance bound value as a float.
"""

import math

def reinforce_var_bound(max_rew, disc, kappa):
    variance_bound = (2 * max_rew * (1 - disc)) / (kappa ** 2)
    return variance_bound