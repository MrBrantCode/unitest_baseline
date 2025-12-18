"""
QUESTION:
Write a function `dijkstra_modified` that implements Dijkstra's algorithm to find the shortest path in a weighted graph where some nodes are temporarily unavailable. The function should take as input a graph represented as an adjacency list, a list of temporarily unavailable nodes, and a start node. The graph's weights are non-negative. The function should return a dictionary with the shortest distances from the start node to all other nodes in the graph.
"""

import heapq

def dijkstra_modified(graph, unavailable_nodes, start_node):
    """
    This function implements Dijkstra's algorithm to find the shortest path 
    in a weighted graph where some nodes are temporarily unavailable.

    Args:
    graph (dict): A dictionary representing the graph as an adjacency list.
    unavailable_nodes (list): A list of nodes that are temporarily unavailable.
    start_node: The node from which to start the search.

    Returns:
    dict: A dictionary with the shortest distances from the start node to all other nodes.
    """

    # Initialize a dictionary with distances from the start node to all other nodes
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0

    # Create a priority queue to store nodes to be processed
    priority_queue = [(0, start_node)]

    while priority_queue:
        # Extract the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current node is temporarily unavailable, skip it
        if current_node in unavailable_nodes:
            continue

        # For each neighbor of the current node
        for neighbor, weight in graph[current_node].items():
            # Calculate the total distance from the start node to the neighbor through the current node
            alternative_distance = current_distance + weight

            # If this distance is less than the current distance, update the distance
            if alternative_distance < distances[neighbor]:
                distances[neighbor] = alternative_distance
                heapq.heappush(priority_queue, (alternative_distance, neighbor))

    return distances