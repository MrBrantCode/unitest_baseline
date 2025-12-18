"""
QUESTION:
Implement the function `min_sum_subtree_values(N, values, edges)` where:
- N: an integer representing the number of nodes in the tree (2 ≤ N ≤ 10^5)
- values: a list of N integers representing the values associated with each node (1 ≤ values[i] ≤ 10^5)
- edges: a list of N-1 tuples representing the edges of the tree. Each tuple (u, v) denotes an edge between nodes u and v (1 ≤ u, v ≤ N)
The function should return an integer representing the minimum sum of values of nodes in a subtree of the given tree.
"""

from collections import defaultdict

def min_sum_subtree_values(N, values, edges):
    adjacency = defaultdict(list)
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)

    mini_sum = float('inf')
    subtree_values = [0] * (N + 1)

    def dfs(src, par):
        nonlocal mini_sum
        subtree_values[src] = values[src - 1]
        count = 0
        for neigh in adjacency[src]:
            if neigh == par:
                continue
            dfs(neigh, src)
            subtree_values[src] += subtree_values[neigh]
        mini_sum = min(mini_sum, subtree_values[src])

    dfs(1, 0)
    return mini_sum