"""
QUESTION:
Write a function named `dfs` that takes a directed graph `graph`, a starting node `start`, a target node `target`, and a maximum path length `max_length` as input. The function should find all possible paths from the starting node to the target node in the graph, subject to the following constraints: 

- The path length must not exceed `max_length`.
- The path must not contain any cycles.
- The path must visit at least one node other than the start and target nodes. 

The graph is represented as a dictionary where each key is a node and its corresponding value is a list of its outgoing edges. The function should return or print all valid paths.
"""

def dfs(graph, start, target, max_length, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [start]

    if start == target and len(path) > 2 and len(path) <= max_length:
        print(path)
        return

    if len(path) > max_length:
        return

    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, target, max_length, visited, path + [neighbor])
    visited.remove(start)