"""
QUESTION:
Create a Python function `shortest_path_and_weight` that takes an adjacency matrix `adj_matrix` representing a simple undirected, weighted graph and two vertices `start` and `end` as input. The function should convert the adjacency matrix into an adjacency list, find the shortest path from `start` to `end` using Dijkstra's algorithm, and return the adjacency list, the shortest path, and the weight of that path. Assume that the graph is connected, vertices exist in the graph, and graph edges have weights from 1 to 100. A value of 0 in the matrix indicates no edge between vertices.
"""

import heapq

def shortest_path_and_weight(adj_matrix, start, end):
    
    # Step 1: Convert adjacency matrix to adjacency list
    adj_list = {node: {} for node in range(len(adj_matrix))}
    
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] != 0:
                adj_list[i][j] = adj_matrix[i][j]

                
    # Step 2: Implement Dijkstra’s algorithm
    shortest_distances = {node: float('inf') for node in range(len(adj_matrix))}
    shortest_distances[start] = 0
    heap = [(0, start)]
    ancestors = {node: None for node in range(len(adj_matrix))}

    while heap:
        dist, node = heapq.heappop(heap)
        
        if dist != shortest_distances[node]:
            continue
            
        for neighbor, weight in adj_list[node].items():
            old_dist = shortest_distances[neighbor]
            new_dist = dist + weight
            
            if new_dist < old_dist:
                shortest_distances[neighbor] = new_dist
                ancestors[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))

    # Step 3: Return shortest path and weight
    path = []
    current = end
    
    while current is not None:
        path.append(current)
        current = ancestors[current]
        
    path = path[::-1]
    weight = shortest_distances[end]
    
    return adj_list, path, weight