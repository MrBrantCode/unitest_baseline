"""
QUESTION:
Write a function `check_self_loop_sum` that takes a directed graph represented as an adjacency matrix `adj` as input and returns `True` if the sum of weights of all self-loops in the graph is zero, and `False` otherwise. The adjacency matrix is a 2D array where the entry at index (i, j) represents the weight of the edge from node i to node j, and the diagonal of the matrix represents self-loops.
"""

from typing import List

def check_self_loop_sum(adj: List[List[int]]) -> bool:
    self_loop_sum = sum(adj[i][i] for i in range(len(adj)))
    return self_loop_sum == 0