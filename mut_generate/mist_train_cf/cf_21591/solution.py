"""
QUESTION:
Implement a function called bellman_ford in Python that finds the shortest path from a source node to all other nodes in a weighted graph, even if the graph contains negative edge weights. The function should take a graph represented as an adjacency list and the source node as input, and return the shortest distances from the source node to all other nodes. The function should also detect and report if there are any negative cycles in the graph.
"""

def bellman_ford(graph, source):
    # Step 1: Prepare the distance for each node
    distance = {node: float('infinity') for node in graph}
    distance[source] = 0

    # Step 2: Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour, neighbour_distance in graph[node].items():
                if distance[node] + neighbour_distance < distance[neighbour]:
                    distance[neighbour] = distance[node] + neighbour_distance

    # Step 3: Check for negative-weight cycles
    for node in graph:
        for neighbour, neighbour_distance in graph[node].items():
            assert distance[node] + neighbour_distance >= distance[neighbour], "Graph contains a negative-weight cycle"

    return distance