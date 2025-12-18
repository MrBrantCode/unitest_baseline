"""
QUESTION:
Design a function `shortest_path(tree, source, destination)` that takes a tree structure represented as an adjacency list (`tree`), a source node (`source`), and a destination node (`destination`) as arguments. The function should return the shortest path between the `source` and `destination` nodes as a list, along with the total number of nodes traversed to reach the destination node. The function must be recursive and handle error scenarios such as missing nodes and cyclical dependencies, and it should be able to handle trees with arbitrarily large numbers of nodes and levels.
"""

def shortest_path(tree, source, destination):
    # Check if both the source and destination nodes are present in the tree
    if source not in tree or destination not in tree:
        return "Source or destination node not found in the tree"

    visited = []

    def dfs(node, dest, path):
        visited.append(node)
        if node == dest:
            return path + [node], len(visited)

        for neighbor in tree[node]:
            if neighbor not in visited:
                new_path, num_nodes = dfs(neighbor, dest, path + [node])
                if new_path is not None:
                    return new_path, num_nodes

        return None, len(visited)

    # Call the helper function with source and destination nodes as arguments
    path, num_nodes = dfs(source, destination, [])

    # If no path was found, return an error message
    if path is None:
        return "No path found between source and destination"

    return path, num_nodes