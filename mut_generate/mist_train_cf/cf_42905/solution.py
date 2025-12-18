"""
QUESTION:
Write a function `optimize_generator_placement(adj_matrix, k)` that takes an adjacency matrix representing a network's transmission costs and the number of generators to be placed `k` as input. The function should return the indices of the optimal nodes to place the generators such that the total cost of power transmission in the network is minimized. The network is represented as an adjacency matrix where `adj_matrix[i][j]` is the cost of transmitting power between nodes `i` and `j`. The indices of the nodes are 0-based.
"""

import numpy as np
from itertools import combinations

def optimize_generator_placement(adj_matrix, k):
    min_cost = float('inf')
    optimal_nodes = []

    # Generate all combinations of k nodes from n
    n = len(adj_matrix)
    node_combinations = list(combinations(range(n), k))

    # Iterate through all combinations and calculate the total cost
    for nodes in node_combinations:
        total_cost = 0
        for i in range(k):
            for j in range(i + 1, k):
                total_cost += adj_matrix[nodes[i]][nodes[j]]

        # Update the optimal nodes if the total cost is minimized
        if total_cost < min_cost:
            min_cost = total_cost
            optimal_nodes = list(nodes)

    return optimal_nodes