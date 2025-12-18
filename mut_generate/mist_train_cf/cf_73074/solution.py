"""
QUESTION:
Implement a function called `delivery_route` that takes as input a graph represented as an adjacency list, and the names of the starting and destination cities, and returns the shortest delivery route between the two cities, assuming the cost of delivery is the same in both directions and does not consider factors such as delivery time, vehicle capacity, or multiple deliveries at once.
"""

import sys
import heapq

def delivery_route(graph, start, destination):
    # Initialize distances to all nodes as infinity except for the start node
    distances = {node: 0 if node == start else sys.maxsize for node in graph}
    previous_nodes = {node: None for node in graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        if current_node == destination:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            path.reverse()
            return path

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return None