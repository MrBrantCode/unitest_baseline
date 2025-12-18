"""
QUESTION:
Develop a function `shortest_path` that computes the shortest path between two nodes in a weighted graph. 

The function should take in a square weighted adjacency matrix `distance_matrix` and two integers `start_node` and `end_node`. The matrix should be a list of lists where each inner list represents a row in the matrix. The value at index i,j represents the weight of the edge between node i and node j.

The function should return a list representing the shortest path between the start and end nodes, considering the weights of the edges. If there is no path between the start and end nodes, the function should return an empty list.
"""

import heapq

def shortest_path(distance_matrix, start_node, end_node):
    num_nodes = len(distance_matrix)
    distances = [float('inf')] * num_nodes
    distances[start_node] = 0

    # Priority queue to keep track of nodes with their distances
    queue = [(0, start_node)]
    heapq.heapify(queue)

    # Parent dictionary to keep track of the shortest path
    parent = {start_node: None}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # If we reach the end node, we have found the shortest path
        if current_node == end_node:
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = parent[current_node]
            return path

        # Iterate over the neighbors of the current node
        for neighbor in range(num_nodes):
            weight = distance_matrix[current_node][neighbor]
            if weight > 0:
                distance = current_distance + weight

                # If we find a shorter distance to a node, update it and enqueue it
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parent[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))

    # If we reach this point, there is no path between the start and end nodes
    return []