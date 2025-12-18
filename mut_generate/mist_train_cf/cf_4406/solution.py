"""
QUESTION:
Implement a function named `dfs` that takes a graph represented as an adjacency list and a starting node, and returns the order in which the nodes were visited during a depth-first search. The function should handle graphs that contain cycles and avoid infinite loops by only visiting unvisited nodes. The graph is represented as a dictionary where each key is a node and its corresponding value is a list of neighboring nodes.
"""

def dfs(graph, start_node):
    visited = []
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            neighbors = graph[node]
            for neighbor in reversed(neighbors):
                stack.append(neighbor)
    
    return visited