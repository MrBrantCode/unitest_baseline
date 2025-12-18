"""
QUESTION:
Implement a function `dfs_traversal(graph, start_vertex)` to perform a depth-first search (DFS) traversal of a directed acyclic graph represented as an adjacency list, starting from the given vertex, and return the order in which the vertices are visited. The graph's vertices are represented as strings.
"""

def dfs_traversal(graph, start_vertex):
    visited = set()
    traversal_order = []

    def dfs_helper(vertex):
        visited.add(vertex)
        traversal_order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs_helper(neighbor)

    dfs_helper(start_vertex)
    return traversal_order