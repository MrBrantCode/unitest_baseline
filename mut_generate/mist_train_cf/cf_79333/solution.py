"""
QUESTION:
Create a function called `countRestrictedPaths` that takes in three parameters: a positive integer `n`, a 2D list `edges` where each sublist contains three elements `[ui, vi, weighti]`, and a 2D list `forbiddenEdges` where each sublist contains two elements `[ui, vi]`. 

Return the number of restricted paths from node `1` to node `n` in an undirected weighted connected graph without using any of the forbidden edges, modulo `10^9 + 7`. 

Constraints:
- `1 <= n <= 2 * 10^4`
- `n - 1 <= edges.length <= 4 * 10^4`
- `edges[i].length == 3`
- `1 <= ui, vi <= n`
- `ui != vi`
- `1 <= weighti <= 10^5`
- There is at most one edge between any two nodes.
- There is at least one path between any two nodes.
- `0 <= m <= 10^4`
- `forbiddenEdges[i].length == 2`
- `1 <= ui, vi <= n`
- `ui != vi`
"""

import heapq
from collections import defaultdict

MOD = 10**9 + 7

def countRestrictedPaths(n, edges, forbiddenEdges):
    graph = defaultdict(list)
    forbidden = set([(min(u,v), max(u,v)) for u, v in forbiddenEdges])
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    distance = [float('inf')] * (n+1)
    distance[n] = 0
    heap = [(0, n)]
    while heap:
        d, node = heapq.heappop(heap)
        if d != distance[node]:
            continue
        for neighbor, w in graph[node]:
            if distance[node] + w < distance[neighbor]:
                distance[neighbor] = distance[node] + w
                heapq.heappush(heap, (distance[neighbor], neighbor))
    dp = [0] * (n + 1)
    dp[n] = 1
    for node in sorted(range(1, n+1), key=lambda i: -distance[i]):
        for neighbor, _ in graph[node]:
            if distance[node] > distance[neighbor] and (min(node, neighbor), max(node, neighbor)) not in forbidden:
                dp[node] += dp[neighbor]
                dp[node] %= MOD
    return dp[1]