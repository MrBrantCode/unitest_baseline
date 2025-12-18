"""
QUESTION:
Implement a function named `dijkstra` that calculates the shortest path between two nodes in a weighted graph using Dijkstra's algorithm. The function should take a weighted graph represented as a dictionary, a starting node, and an ending node as inputs. The graph dictionary should have nodes as keys and dictionaries of neighboring nodes with their corresponding weights as values. The function should return the shortest distance from the starting node to the ending node. If there is no path from the starting node to the ending node, the function should return infinity.
"""

import heapq

def dijkstra(graph, start_node, end_node):
    distances = {}
    for node in graph:
        distances[node] = float('inf')
    distances[start_node] = 0
    
    visited = set()
    unvisited = [(0, start_node)]
    
    while unvisited:
        current_distance, current_node = heapq.heappop(unvisited)
        visited.add(current_node)
        
        if current_node == end_node:
            return distances[end_node]
        
        for neighbor, distance in graph[current_node].items():
            if neighbor in visited:
                continue
            
            new_distance = current_distance + distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(unvisited, (new_distance, neighbor))
                
    return float('inf')