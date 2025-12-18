"""
QUESTION:
Create a function `shortest_path(graph, starting_vertex, end_vertex)` that finds the shortest weighted path between any two nodes in a tree represented as an adjacency list. The function should take a weighted tree graph, a starting vertex, and an end vertex as input and return the shortest distance between the two vertices. The function should use Dijkstra's algorithm and have a time complexity of at least O(V^2) or better.
"""

from heapq import heappop, heappush

def shortest_path(graph, starting_vertex, end_vertex):
    shortest_distances = {vertex: float('infinity') for vertex in graph}
    shortest_distances[starting_vertex] = 0
    heap = [(0, starting_vertex)]
    while heap:
        curr_dist, curr_vertex = heappop(heap)
        if curr_dist > shortest_distances[curr_vertex]:
            continue
        for neighbor, weight in graph[curr_vertex].items():
            distance = curr_dist + weight
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heappush(heap, (distance, neighbor))
    return shortest_distances[end_vertex]