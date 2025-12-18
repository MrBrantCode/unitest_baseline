"""
QUESTION:
Write a function named `dfs` that implements a Depth First Search (DFS) algorithm to find all possible paths from a starting node to a target node in a directed graph. The function should take as input the starting node and the target node, and return a list of all possible paths. Assume that the graph is represented as an adjacency list and the nodes are numbered from 0 to V-1, where V is the number of vertices in the graph.
"""

def dfs(graph, source, target):
    """
    Finds all possible paths from a starting node to a target node in a directed graph.

    Args:
    graph: Adjacency list representation of the graph.
    source: Starting node.
    target: Target node.

    Returns:
    A list of all possible paths from the source node to the target node.
    """
    visited = [False] * len(graph)
    path = []
    all_paths = []
    dfs_util(graph, source, target, visited, path, all_paths)
    return all_paths

def dfs_util(graph, u, target, visited, path, all_paths):
    """
    Recursive utility function to perform DFS traversal.
    """
    visited[u] = True
    path.append(u)
    if u == target:
        all_paths.append(list(path))
    else:
        for v in graph[u]:
            if not visited[v]:
                dfs_util(graph, v, target, visited, path, all_paths)
    path.pop()
    visited[u] = False