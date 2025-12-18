"""
QUESTION:
Implement a function `bfs_shortest_path(graph, start, end)` to find the shortest path between two nodes in a weighted graph using a breadth-first search algorithm. The function should take a weighted graph represented as an adjacency list, a start node, and an end node as input, and return a list of nodes representing the shortest path from the start to the end node. If there is no path, return None. The graph is represented as a dictionary where the keys are nodes and the values are lists of tuples representing the neighboring nodes and their corresponding weights.
"""

from collections import deque

def bfs_shortest_path(graph, start, end):
    queue = deque()
    queue.append(start)
    
    visited = set()
    visited.add(start)
    
    distance = {start: 0}
    
    previous = {start: None}
    
    while queue:
        node = queue.popleft()
        
        if node == end:
            path = []
            while node:
                path.append(node)
                node = previous[node]
            return list(reversed(path))
        
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                distance[neighbor] = distance[node] + weight
                previous[neighbor] = node
    
    return None