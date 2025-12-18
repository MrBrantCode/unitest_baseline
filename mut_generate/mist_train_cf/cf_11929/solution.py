"""
QUESTION:
Implement a depth-first search (DFS) function in Python, `dfs(graph, start)`, that performs a depth-first search on a given graph starting from a specified node. The graph is represented as an adjacency list where each key is a node and its corresponding value is a list of neighboring nodes. The function should return a list of visited nodes in the order they were visited.
"""

def dfs(graph, start):
    """
    Performs a depth-first search on a given graph starting from a specified node.

    Args:
    graph (dict): A graph represented as an adjacency list.
    start (node): The node to start the search from.

    Returns:
    list: A list of visited nodes in the order they were visited.
    """
    visited = set()
    result = []

    def dfs_helper(node):
        visited.add(node)
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)

    dfs_helper(start)
    return result