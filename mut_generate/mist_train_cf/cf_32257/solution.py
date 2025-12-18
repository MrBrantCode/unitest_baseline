"""
QUESTION:
Implement a function `depth_first_search(graph, start_node)` that performs a depth-first search on a given graph and returns the order in which the nodes are visited. The graph is represented as a dictionary where the keys are the nodes and the values are lists of adjacent nodes. The function should take the graph and the starting node as input and return a list of nodes in the order they were visited. The graph may contain cycles, and each node should be visited only once.
"""

def depth_first_search(graph, start_node):
    visited = set()

    def dfs_helper(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)

    dfs_helper(start_node)
    return list(visited)