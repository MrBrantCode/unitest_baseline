"""
QUESTION:
Develop a function named `shortest_path` that takes in a weighted adjacency matrix and two integers representing the start and end nodes of the route. The function should return a list representing the shortest path between the start and end nodes, considering the weights of the edges. If there is no path between the start and end nodes, the function should return an empty list. The weighted adjacency matrix is a square matrix represented as a list of lists, where each inner list represents a row in the matrix and the value at index i, j represents the weight of the edge between node i and node j.
"""

import heapq

def shortest_path(distance_matrix, start_node, end_node):
    num_nodes = len(distance_matrix)
    distances = [float('inf')] * num_nodes
    distances[start_node] = 0

    queue = [(0, start_node)]
    heapq.heapify(queue)

    parent = {start_node: None}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == end_node:
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = parent[current_node]
            return path

        for neighbor in range(num_nodes):
            weight = distance_matrix[current_node][neighbor]
            if weight > 0:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parent[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))

    return []