"""
QUESTION:
Implement the function `dijkstra_shortest_path(graph, source)` that finds the shortest path from a given source node to all other nodes in a graph using Dijkstra's algorithm. The graph is represented as a list of edges where each edge is a tuple in the format (source, destination, weight) with source and destination as integers and weight as a positive integer. The function should return a dictionary containing the shortest distance from the source to each node in the graph, with unreachable nodes represented as infinity.
"""

import heapq

def dijkstra_shortest_path(graph, source):
    distances = {node: float('inf') for edge in graph for node in edge[:2]}
    distances[source] = 0
    queue = [(0, source)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for edge in graph:
            if edge[0] == current_node:
                neighbor, weight = edge[1], edge[2]
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

    return distances