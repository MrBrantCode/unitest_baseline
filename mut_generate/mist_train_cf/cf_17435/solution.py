"""
QUESTION:
Implement a function `bfs` to find the shortest path between two nodes in a weighted graph with negative weights and cycles. The function should take an adjacency list representation of the graph, a start node, and an end node as input, and return the shortest distance between the start and end nodes.
"""

from collections import deque
import math

def bfs(graph, start, end):
    distances = [math.inf] * len(graph)
    distances[start] = 0
    visited = [False] * len(graph)

    queue = deque([(start, 0)])

    while queue:
        node, curr_weight = queue.popleft()

        if visited[node]:
            continue

        visited[node] = True

        for neighbor, weight in graph[node]:
            new_weight = curr_weight + weight

            if new_weight < distances[neighbor]:
                distances[neighbor] = new_weight
                queue.append((neighbor, new_weight))

    return distances[end]