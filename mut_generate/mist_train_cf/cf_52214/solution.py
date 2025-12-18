"""
QUESTION:
Given a directed graph represented by `edges` where `edges[i] = [ai, bi]` signifies an edge between nodes `ai` and `bi`, and two nodes `source` and `destination`, write a function `solve(n: int, edges: List[List[int]], source: int, destination: int)` that returns `True` if all paths from `source` ultimately lead to `destination`, and `False` otherwise. The graph may contain self-loops and parallel edges, and `1 <= n <= 10^4`, `0 <= edges.length <= 10^4`, `0 <= ai, bi <= n - 1`, `0 <= source <= n - 1`, `0 <= destination <= n - 1`.
"""

from typing import List

global UNVISITED, VISITED
UNVISITED, VISITED = -1, 1

def solve(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    graph = [[] for _ in range(n)]
    state = [UNVISITED] * n
    for u, v in edges:
        graph[u].append(v)

    def dfs(node):
        if state[node] == VISITED:
            return True
        if node != destination and len(graph[node]) == 0:
            return False
        state[node] = VISITED
        for child in graph[node]:
            if state[child] == UNVISITED and not dfs(child):
                return False
        return node == destination or len(graph[node]) > 0

    return dfs(source)