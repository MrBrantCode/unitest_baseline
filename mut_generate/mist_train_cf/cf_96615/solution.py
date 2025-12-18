"""
QUESTION:
Write a function `dfs_paths(graph, start, target, max_length)` that uses Depth First Search (DFS) to find all possible paths from a starting node `start` to a target node `target` in a directed graph `graph` with a maximum path length of `max_length`. The graph is represented as an adjacency list, where each key is a node and the corresponding value is a list of its neighboring nodes.
"""

def dfs_paths(graph, start, target, max_length):
    visited = set()  # Track visited nodes
    paths = []  # Track valid paths

    def dfs(current_node, path):
        visited.add(current_node)
        path.append(current_node)

        # If the target node is reached and the path length is within the constraint
        if current_node == target and len(path) <= max_length:
            paths.append(path[:])  # Add a copy of the current path to the valid paths

        # If the current path length exceeds the maximum length constraint
        if len(path) > max_length:
            return

        # Recurse on the neighbors of the current node
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                dfs(neighbor, path)

        path.pop()  # Remove the current node from the path
        visited.remove(current_node)

    dfs(start, [])
    return paths