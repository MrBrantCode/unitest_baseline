"""
QUESTION:
Implement a function called `dijkstra_algorithm` that calculates the shortest path in a graph with non-negative edge weights. The function should take a graph represented as an adjacency matrix and a starting vertex as input. The function should return a dictionary with the shortest distances from the starting vertex to all other vertices.
"""

import sys
import heapq

def dijkstra_algorithm(graph, start):
    """
    This function calculates the shortest path in a graph with non-negative edge weights.
    
    Args:
        graph (list of lists): A 2D list representing the adjacency matrix of the graph.
        start (int): The starting vertex.
        
    Returns:
        dict: A dictionary with the shortest distances from the starting vertex to all other vertices.
    """
    
    # Initialize a dictionary to store the shortest distances
    distances = {i: sys.maxsize for i in range(len(graph))}
    distances[start] = 0  # The distance to the start node is 0
    
    # Initialize a priority queue with the start node
    pq = [(0, start)]  # The priority is the distance
    
    while pq:
        # Extract the vertex with the smallest distance from the priority queue
        current_distance, current_vertex = heapq.heappop(pq)
        
        # If the current distance is greater than the already found distance, skip this vertex
        if current_distance > distances[current_vertex]:
            continue
        
        # For the extracted vertex, examine its neighbors
        for neighbor, weight in enumerate(graph[current_vertex]):
            if weight > 0:
                distance = current_distance + weight
                
                # If the distance of the neighbor using the current edge is less than its current distance, update the current distance
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
    
    return distances