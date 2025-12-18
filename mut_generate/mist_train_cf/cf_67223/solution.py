"""
QUESTION:
Implement a function `shortest_path(graph, start, end)` that takes a weighted graph represented as an adjacency list and two nodes `start` and `end` as input, and returns a tuple containing the shortest distance from `start` to `end` and the corresponding path. The graph is represented as a dictionary where each key is a node and its corresponding value is another dictionary with neighboring nodes as keys and edge weights as values. The function should be able to handle graphs with non-negative edge weights and should return the shortest distance and path if a path exists, otherwise, it should return infinity for the distance and an empty path.
"""

import sys
import heapq

def shortest_path(graph, start, end):
    heap = [(0, start)]
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    paths = {start: [start]}

    while heap:
        (curr_distance, curr_vertex) = heapq.heappop(heap)
        for neighbor, neighbor_distance in graph[curr_vertex].items():
            distance = curr_distance + neighbor_distance
            if distance < distances[neighbor]: 
                distances[neighbor] = distance
                paths[neighbor] = paths[curr_vertex] + [neighbor]
                heapq.heappush(heap, (distance, neighbor))

    if distances[end] == float('infinity'):
        return float('inf'), []
    return distances[end], paths[end]