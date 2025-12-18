"""
QUESTION:
Write a function `shortest_path_digraph` that finds the shortest path in a randomly directed graph. The function should operate within a logarithmic time complexity.
"""

import heapq

def shortest_path_digraph(graph, start, end):
    """
    Finds the shortest path in a directed graph from a start node to an end node.
    
    Args:
    graph (dict): A dictionary representing the graph, where each key is a node and its corresponding value is another dictionary with neighboring nodes and their respective edge weights.
    start (str): The node to start the search from.
    end (str): The node to find the shortest path to.
    
    Returns:
    list: A list of nodes representing the shortest path from the start node to the end node.
    """

    # Initialize a dictionary to store the distance to each node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Initialize a dictionary to store the previous node in the shortest path
    previous = {node: None for node in graph}

    # Initialize a priority queue with the start node
    priority_queue = [(0, start)]

    # Loop through the priority queue
    while priority_queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current node is the end node, we've found the shortest path
        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous[current_node]
            path.reverse()
            return path

        # If the current distance is greater than the stored distance, skip this node
        if current_distance > distances[current_node]:
            continue

        # For each neighbor of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If this path is shorter than the stored distance, update the distance and previous node
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))