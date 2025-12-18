"""
QUESTION:
Implement a function `dfs(graph, start_node)` that performs a Depth-First-Search (DFS) traversal on a given graph represented as an adjacency list. The function should take in the graph and the starting node as parameters and return the order in which the nodes are visited during the DFS traversal. 

The graph is represented as a dictionary where each key is a node and its corresponding value is a list of adjacent nodes. The function should handle cases where the graph is empty or the starting node is not present in the graph. 

Assume that the graph may contain cycles and there are no weights on the edges.
"""

def dfs(graph, start_node):
    # Check if the graph is empty or the starting node is not present
    if not graph or start_node not in graph:
        return []

    visited = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            # Add unvisited adjacent nodes to the stack
            stack.extend(graph[node])

    return visited