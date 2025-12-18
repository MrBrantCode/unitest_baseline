"""
QUESTION:
Implement a map routing system using graph theory and shortest path algorithms. Define a function `map_routing` that takes a graph representing the map and two nodes (start and end points) as input, and returns the shortest path between the two nodes. The graph should be represented as an adjacency list, and the function should use Dijkstra's algorithm or A* algorithm to find the shortest path.
"""

import sys
import heapq

def map_routing(graph, start, end):
    """
    This function implements Dijkstra's algorithm to find the shortest path between two nodes in a graph.

    Args:
    graph (dict): The input graph represented as an adjacency list.
    start (str): The starting node.
    end (str): The ending node.

    Returns:
    list: The shortest path from the start node to the end node.
    """

    # Initialize distances to all nodes as infinity except for the start node
    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0

    # Initialize the priority queue with the start node
    priority_queue = [(0, start)]

    while priority_queue:
        # Extract the node with the minimum distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current node is the end node, we have found the shortest path
        if current_node == end:
            return distances

        # If the current distance is greater than the already found distance, skip this node
        if current_distance > distances[current_node]:
            continue

        # Iterate over the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            # Calculate the distance to the neighbor
            distance = current_distance + weight

            # If this distance is less than the already found distance, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    # If there is no path to the end node, return None
    return None