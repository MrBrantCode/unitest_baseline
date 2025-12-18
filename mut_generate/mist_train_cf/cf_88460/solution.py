"""
QUESTION:
Implement a function called `dfs` that performs a depth-first search on a graph. The function should take two parameters: `graph`, which is a dictionary representing the graph as an adjacency list, and `start_node`, which is the node in the graph where the search should begin. The function should return a list of nodes in the order they were visited. The graph may contain cycles, and the function should be able to detect and handle them correctly.
"""

def dfs(graph, start_node):
    visited = []
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                stack.append(neighbor)
    
    return visited