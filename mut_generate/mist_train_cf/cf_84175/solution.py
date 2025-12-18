"""
QUESTION:
Write a function `shortest_cycle(graph)` that takes an undirected graph represented as an adjacency list and returns the length of the shortest cycle in the graph. The graph is represented as a list of lists where `graph[i]` is a list of all vertices adjacent to vertex `i`. The function should return `-1` if the graph does not contain any cycles. The function must run in polynomial time.
"""

from collections import deque

def shortest_cycle(graph):
    shortest = float('inf')
    for source in range(len(graph)):
        queue = deque()
        queue.append((source, -1, 0))  # (vertex, parent, depth)
        visited = [0] * len(graph)
        visited[source] = 1
        while queue:
            vertex, parent, depth = queue.popleft()
            for neighbor in graph[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = 1
                    queue.append((neighbor, vertex, depth + 1))
                elif neighbor != parent:
                    shortest = min(shortest, depth + 1)
    return -1 if shortest == float('inf') else shortest