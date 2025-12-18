"""
QUESTION:
Implement a function `BFS` and `DFS` that performs Breadth-First Search and Depth-First Search respectively on a tree data structure represented as an adjacency list. The function should take the adjacency list `graph` and the `root` node as input and return the order of visited nodes. The tree can have any number of nodes and the Depth-First Search should consider left-most children first.
"""

from collections import deque

def BFS(graph, root):
    visited = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    
    return visited

def DFS(graph, root, visited = None):
    if visited is None:
        visited = []
    visited.append(root)
    
    for node in graph[root]:
        if node not in visited:
            DFS(graph, node, visited)
    
    return visited