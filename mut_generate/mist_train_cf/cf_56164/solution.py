"""
QUESTION:
Implement a function called `shortest_path` that uses Dijkstra's Algorithm to find the shortest path from a source vertex to all other vertices in a weighted graph with non-negative edge weights. The function should take in a graph represented as a dictionary where the keys are the nodes and the values are dictionaries of neighboring nodes and their respective edge weights, as well as a start node and an end node. The function should return the shortest distance from the start node to the end node. The graph can contain multiple paths between nodes, and the function should always choose the path with the shortest total edge weight.
"""

import sys
import heapq

def shortest_path(graph, start, end):
    """
    This function uses Dijkstra's Algorithm to find the shortest distance from a source vertex to all other vertices in a weighted graph.

    Args:
    graph (dict): A dictionary representing the graph where keys are the nodes and values are dictionaries of neighboring nodes and their respective edge weights.
    start (node): The source node.
    end (node): The target node.

    Returns:
    float: The shortest distance from the start node to the end node.
    """
    heap = [(0, start)]
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    while heap:
        (dist, current) = heapq.heappop(heap)
        if current == end:
            return distances[end]
        for neighbor, distance in graph[current].items():
            old_distance = distances[neighbor]
            new_distance = dist + distance
            if new_distance < old_distance:
                distances[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))
    return None