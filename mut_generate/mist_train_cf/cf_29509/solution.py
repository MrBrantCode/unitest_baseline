"""
QUESTION:
Implement a function `dijkstra_shortest_path(graph, weights, source)` that uses Dijkstra's algorithm to find the shortest path from a given source node to all other nodes in a directed graph. The function takes three inputs:
- `graph`: a dictionary representing the directed graph, where keys are nodes and values are lists of tuples representing outgoing edges and their destination nodes.
- `weights`: a dictionary that maps edges to their respective weights.
- `source`: the source node from which to find the shortest paths.
 
The function should return a dictionary where the keys are the destination nodes and the values are the shortest distances from the source node to the respective destination nodes.
"""

import heapq

def dijkstra_shortest_path(graph, weights, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    heap = [(0, source)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weights[(current_node, neighbor)]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances