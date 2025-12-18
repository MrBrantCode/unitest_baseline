"""
QUESTION:
Implement a breadth-first search function `bfs` that efficiently traverses a large graph, taking a graph and a start node as input, and returning a set of visited nodes. Use an efficient data structure for the queue and keep track of visited nodes to minimize overhead. Assume the graph is represented as an adjacency list.
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