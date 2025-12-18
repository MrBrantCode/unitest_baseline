"""
QUESTION:
Implement the `transitive_reduce` function that takes a directed graph represented as an adjacency matrix `A` of size `n x n` as input and returns the transitive reduction of the graph. The input adjacency matrix `A` is a boolean matrix where `A[i][j]` is `True` if there is a directed edge from node `i` to node `j`, and `False` otherwise. The function should return the transitive reduction of the input graph as a new adjacency matrix. The transitive reduction of a directed graph is obtained by removing any edges that can be inferred from the remaining edges in the graph.
"""

import numpy as np

def transitive_reduction(A):
    n = len(A)
    A_red = np.copy(A)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if A_red[i][k] and A_red[k][j]:
                    A_red[i][j] = False

    return A_red