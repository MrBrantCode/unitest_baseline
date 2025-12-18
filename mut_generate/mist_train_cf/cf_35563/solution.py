"""
QUESTION:
Implement a function `sinkhorn_divergence` that calculates the Sinkhorn divergence between two probability distributions. The function takes the weights and supports of two clusters, as well as a regularization parameter epsilon, and returns their Sinkhorn divergence.

Input:
- `a`: A list of floats representing the weights of the first cluster
- `x`: A list of floats representing the support of the first cluster
- `b`: A list of floats representing the weights of the second cluster
- `y`: A list of floats representing the support of the second cluster
- `epsilon`: A float representing the regularization parameter

Output:
- A float representing the Sinkhorn divergence between the two clusters

Assume that the input lists `a`, `x`, `b`, and `y` are of the same length.
"""

from typing import List
import numpy as np

def sinkhorn_divergence(a: List[float], x: List[float], b: List[float], y: List[float], epsilon: float) -> float:
    n = len(a)
    m = len(b)
    cost_matrix = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            cost_matrix[i, j] = -epsilon * (x[i] - y[j])**2  # Example cost function: squared Euclidean distance

    K = np.exp(cost_matrix / epsilon)
    u = np.ones(n)
    v = np.ones(m)
    for _ in range(100):  # Number of Sinkhorn iterations
        u = a / (K @ v)
        v = b / (K.T @ u)

    sinkhorn_div = np.sum(u * (K @ v))
    return sinkhorn_div