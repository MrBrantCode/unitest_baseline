"""
QUESTION:
Implement the `leaky_integration` function to compute the current state `y(t)` in an echo state network. The function should take in the following parameters: the leaky rate (a float between 0 and 1), the past state `y(t-1)`, the input at time `t` (`u(t)`), the input weights `Win`, and the recurrent weights `W`. The function should use the `tanh` activation function.
"""

import numpy as np

def leaky_integration(leaky, y_prev, u, Win, W):
    """
    Compute the current state y(t) in an echo state network using leaky integration.

    Parameters:
    leaky (float): The leaky rate between 0 and 1.
    y_prev (numpy array): The past state y(t-1).
    u (numpy array): The input at time t.
    Win (numpy array): The input weights.
    W (numpy array): The recurrent weights.

    Returns:
    numpy array: The current state y(t).
    """
    return (1 - leaky) * y_prev + leaky * np.tanh(np.dot(Win, u) + np.dot(W, y_prev))