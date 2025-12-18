"""
QUESTION:
Write a function `shortestPath(graph)` that takes a weighted directed acyclic graph (DAG) of `n` nodes as input, where `graph[i]` is a list of tuples containing the node that can be visited from node `i` and the weight of the edge. The function should return the shortest path from node `0` to node `n - 1`. 

Note: The input graph is guaranteed to be a DAG with `2 <= n <= 15` nodes and `1 <= graph[i][j][1] <= 10` edge weights.
"""

def shortestPath(graph):
    n = len(graph)
    dp = [None] * n  # distances from node 0 to all other nodes
    dp[0] = (0, [0])  # distance and path to node 0
    for node in range(n):
        if dp[node] is None:
            continue
        d, path = dp[node]
        for nei, nei_distance in graph[node]:
            if dp[nei] is None or d + nei_distance < dp[nei][0]:
                dp[nei] = d + nei_distance, path + [nei]
    return dp[-1][1]  