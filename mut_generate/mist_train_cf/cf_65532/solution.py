"""
QUESTION:
Implement a function called `pagerank` that calculates the PageRank of a given transition matrix `M` using the power iteration method. The function should take in the transition matrix `M`, the number of iterations `num_iterations` (default value is 100), and the damping factor `d` (default value is 0.85). The function should return a vector representing the PageRank of each web page. Assume that the input matrix `M` is a column-stochastic matrix.
"""

import numpy as np

def pagerank(M, num_iterations=100, d=0.85):
    N = M.shape[1]
    v = np.random.rand(N, 1)
    v = v / np.linalg.norm(v, 1)
    iteration = 0
    while iteration < num_iterations:
        iteration += 1
        v = d * np.matmul(M, v) + (1 - d) / N
    return v