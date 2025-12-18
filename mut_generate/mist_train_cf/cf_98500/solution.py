"""
QUESTION:
Implement a function `bfs` that performs a breadth-first search on a given graph, starting from a specified node. The graph is represented as a dictionary where each key is a node and its corresponding value is a list of neighboring nodes. The function should return a set of all visited nodes. The function should be optimized for performance on large graphs.
"""

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited