"""
QUESTION:
Implement the `dfs` function that performs a depth-first search on a graph represented as an adjacency list. The function should take in the adjacency list `graph` and a `start_node`, and return the order in which the nodes were visited during the search. The adjacency list `graph` is represented as a dictionary where each key is a node and its value is a list of its neighboring nodes.
"""

def dfs(graph, start_node):
    visited = set()
    traversal_order = []

    def dfs_helper(node):
        visited.add(node)
        traversal_order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)

    dfs_helper(start_node)
    return traversal_order