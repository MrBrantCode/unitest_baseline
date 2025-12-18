"""
QUESTION:
Implement an iterative Depth-First Search algorithm using a stack data structure, with the following requirements: 
- The algorithm should have a time complexity of O(V + E), where V is the number of vertices and E is the number of edges in the graph.
- The algorithm should have a space complexity of O(V), where V is the number of vertices in the graph.
- Assume the graph is represented using an adjacency list and implement the function `dfs_iterative` that takes a graph `G` and a starting vertex `start` as input and returns a set of visited vertices.
"""

def dfs_iterative(G, start):
    """
    Performs an iterative Depth-First Search on a graph using a stack data structure.

    Args:
    G (dict): The graph represented as an adjacency list.
    start (node): The starting vertex for the DFS traversal.

    Returns:
    set: A set of visited vertices.
    """
    stack = [start]
    visited = set()
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in G[vertex]:
                stack.append(neighbor)
    
    return visited