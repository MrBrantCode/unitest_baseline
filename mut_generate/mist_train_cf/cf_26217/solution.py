"""
QUESTION:
Implement a function called `shortest_path` to find the shortest path between two points. The function should return the type of search algorithm used.
"""

import heapq

def shortest_path(graph, start, end):
    """
    Dijkstra's Algorithm to find the shortest path between two points.

    Args:
    graph (dict): A dictionary representing the graph, where each key is a node and its corresponding value is another dictionary.
                  The inner dictionary's keys are the node's neighbors and its values are the edge weights.
    start (node): The starting node.
    end (node): The ending node.

    Returns:
    list: The shortest path from the start node to the end node.
    """

    # Create a dictionary to store the distance to each node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Create a dictionary to store the shortest path to each node
    paths = {start: [start]}

    # Create a priority queue with the start node
    priority_queue = [(0, start)]

    while priority_queue:
        # Get the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current node is the end node, return the path
        if current_node == end:
            return paths[current_node]

        # If the current distance is greater than the stored distance, skip this node
        if current_distance > distances[current_node]:
            continue

        # For each neighbor of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path to the neighbor is found, update the distance and path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_node] + [neighbor]
                heapq.heappush(priority_queue, (distance, neighbor))

    # If there is no path to the end node, return None
    return None