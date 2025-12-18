"""
QUESTION:
Implement a `calculate_shortest_path` method within the `RouteService` class that takes a graph, start location, and end location as input and returns the shortest path as a list of locations using Dijkstra's algorithm. The method should use a dictionary to represent the graph where each key is a node and its corresponding value is another dictionary containing the neighboring nodes and their respective edge weights. The method should return an empty list if the start or end location is not in the graph.
"""

def calculate_shortest_path(graph, start, end):
    """
    This function calculates the shortest path in a graph using Dijkstra's algorithm.
    
    Args:
    graph (dict): A dictionary representing the graph where each key is a node and its corresponding value is another dictionary containing the neighboring nodes and their respective edge weights.
    start (str): The starting location.
    end (str): The ending location.
    
    Returns:
    list: A list of locations representing the shortest path from the start to the end location. If the start or end location is not in the graph, an empty list is returned.
    """

    # Check if start or end location is not in the graph
    if start not in graph or end not in graph:
        return []

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    unvisited_nodes = set(graph)

    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: distances[node])
        unvisited_nodes.remove(current_node)

        for neighbor, weight in graph[current_node].items():
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    path = []
    current_node = end
    while current_node != start:
        path.insert(0, current_node)
        for neighbor, weight in graph[current_node].items():
            if distances[current_node] == distances[neighbor] + weight:
                current_node = neighbor
                break
    path.insert(0, start)
    return path