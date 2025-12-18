"""
QUESTION:
Implement a function `dfs(graph, start, end)` that performs a depth-first search on a graph to check if there is a path from the `start` node to the `end` node. The `graph` is represented as an adjacency list where `graph[i]` contains a list of neighboring nodes of node `i`. The function should return `True` if a path exists and `False` otherwise.
"""

def dfs(graph, start, end):
    visited = [False] * len(graph)
    stack = [start]
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            if node == end:
                return True
            stack.extend(neighbor for neighbor in graph[node] if not visited[neighbor])
    
    return False