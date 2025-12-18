"""
QUESTION:
Implement the function `shortestPath(graph, start, end)` that finds the shortest path between two nodes in a weighted graph, where the graph can contain negative weights and cycles. The function takes as input a weighted graph represented as an adjacency list `graph`, the start node `start`, and the end node `end`. The function should return the shortest distance between the start and end nodes. The graph nodes are 0-indexed.
"""

from collections import deque
import math

def shortestPath(graph, start, end):
    distances = [math.inf] * len(graph)
    distances[start] = 0

    queue = deque([(start, 0)])

    while queue:
        node, curr_weight = queue.popleft()

        if distances[node] < curr_weight:
            continue

        for neighbor, weight in graph[node]:
            new_weight = curr_weight + weight

            if new_weight < distances[neighbor]:
                distances[neighbor] = new_weight
                queue.append((neighbor, new_weight))

    return distances[end]