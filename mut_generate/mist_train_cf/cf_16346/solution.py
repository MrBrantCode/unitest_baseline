"""
QUESTION:
Implement a function `dfs(graph, start_node)` that performs a Depth-First-Search (DFS) traversal on a given graph represented as an adjacency list. The function should take the graph and the starting node as parameters, and return the order in which the nodes are visited during the DFS traversal. 

The function should handle cases where the graph is empty or the starting node is not present in the graph, and should have a time complexity of O(V + E) and space complexity of O(V), where V is the number of vertices and E is the number of edges in the graph.
"""

def entrance(graph, start_node):
    if not graph or start_node not in graph:
        return []

    visited = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    return visited