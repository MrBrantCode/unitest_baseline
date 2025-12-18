"""
QUESTION:
Implement a function named `dfs_traversal` that performs a depth-first search traversal of a graph represented as an adjacency list, starting from a given node, and returns a list of visited nodes. The graph is represented as a dictionary in the form {node: [neighbors]} and the function should avoid visiting the same node multiple times.
"""

def dfs_traversal(graph, start_node):
    visited_nodes = set()

    def dfs_util(node):
        visited_nodes.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited_nodes:
                dfs_util(neighbor)

    dfs_util(start_node)
    return list(visited_nodes)