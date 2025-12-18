"""
QUESTION:
Implement a function called `Dijkstra` that uses Dijkstra's algorithm to find the shortest path in a graph with non-negative edge weights. The function should take as input a graph represented as an adjacency list and a starting node, and return a tuple containing the shortest distances from the starting node to all other nodes and the previous node that leads to each node. The function should have a maximum time complexity of O(n log n).
"""

import heapq

def Dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, previous