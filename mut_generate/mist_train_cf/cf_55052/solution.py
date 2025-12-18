"""
QUESTION:
Implement a function named `dijkstra` that takes a graph and a source node as input, and returns a dictionary containing the shortest distance from the source node to all other nodes in the graph. The graph should be represented as a dictionary where each key is a node and its corresponding value is another dictionary representing the edges and their weights. The function should use a greedy algorithm to determine the shortest distances.
"""

def dijkstra(graph, source):
    distance = {node: float('infinity') for node in graph}
    distance[source] = 0
    unvisited = list(graph)

    while unvisited:
        current_node = min(
            unvisited, key=lambda node: distance[node]
        )
        unvisited.remove(current_node)

        for neighbour, distance_to_neighbour in graph[current_node].items():
            old_distance = distance[neighbour]
            new_distance = distance[current_node] + distance_to_neighbour
            distance[neighbour] = min(old_distance, new_distance)

    return distance