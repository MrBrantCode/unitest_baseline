"""
QUESTION:
Given a function `countIsolatedNodes(n, edges, query)` that takes an integer `n` representing the number of nodes, a list of edges where each edge is a list `[u, v]` denoting an undirected edge between `u` and `v`, and an integer `query`, return the count of nodes with edge count less than or equal to `query`. The function must handle repeated edges and satisfy the constraints: `2 <= n <= 2 * 10^4`, `1 <= edges.length <= 10^5`, `1 <= u, v <= n`, `u != v`, and `0 <= query <= edges.length`.
"""

def countIsolatedNodes(n, edges, query):
    edge_count = [0] * (n + 1)
    for u, v in edges:
        edge_count[u] += 1
        edge_count[v] += 1
    
    return sum(1 for count in edge_count[1:] if count <= query)