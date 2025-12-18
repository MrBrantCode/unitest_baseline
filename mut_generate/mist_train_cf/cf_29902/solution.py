"""
QUESTION:
Implement a function `shortest_path(graph, start, target)` that takes a directed graph represented as an adjacency list, a starting node `start`, and a target node `target`, and returns a tuple `(path, weight)` representing the shortest path from `start` to `target` and its total weight. If no such path exists, return `None`. 

The graph is represented as a dictionary where each key is a node and its corresponding value is a list of tuples, each containing a neighboring node and the edge weight.
"""

import heapq

def shortest_path(graph, start, target):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    queue = [(0, start)]
    
    parent = {start: None}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == target:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            return path, distances[target]

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                parent[neighbor] = current_node

    return None