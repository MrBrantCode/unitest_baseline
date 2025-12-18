"""
QUESTION:
Given a graph with N nodes represented as an adjacency list, write a function `max_depth(graph, N, target_node)` that returns the maximum depth of the graph starting from a given target node. The graph is represented as a list of lists, where `graph[i]` contains a list of nodes adjacent to node `i`. The function should return the number of edges in the longest path from the target node to any leaf node.
"""

from typing import List

def max_depth(graph: List[List[int]], N: int, target_node: int) -> int:
    visited = [False] * N
    depth = [0] * N

    def dfs(node, d):
        visited[node] = True
        depth[node] = d
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, d + 1)

    dfs(target_node, 0)
    return max(depth)