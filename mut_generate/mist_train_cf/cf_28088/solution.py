"""
QUESTION:
Implement the function `calculate_communication_cost(w, tau_p, shita)` that calculates the total communication cost incurred in a distributed computing system. The function takes a 3D numpy array `w` representing the weights between nodes, a 1D numpy array `tau_p` representing the threshold values for each node, and a scalar value `shita` representing a constant threshold. The function should return the total communication cost. 

The function should iterate through each node `p` from 1 to P-1, compare the square of `w[p]` with `tau_p[p] * shita`, and increment the communication cost by 1 for each index `n` where the condition is true, assuming a function `send_to1(n, w[p, n])` is called for each such index.
"""

import numpy as np

def calculate_communication_cost(w, tau_p, shita):
    P, N, _ = w.shape
    communication_cost = 0

    for p in range(1, P):
        candidate = np.where(np.square(w[p]) > tau_p[p] * shita)[0]
        communication_cost += len(candidate)

    return communication_cost