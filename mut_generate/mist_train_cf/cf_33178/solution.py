"""
QUESTION:
Write a function `is_fully_connected(matrix)` that takes a symmetric matrix as input, where each cell contains a 0 or 1 indicating whether there is a connection between the corresponding nodes. The function should return `True` if there is a path between every pair of nodes, and `False` otherwise. The input matrix is guaranteed to be square and contain only 0s and 1s.
"""

def is_fully_connected(matrix):
    n = len(matrix)

    # Create a set of nodes to be visited
    to_visit = set(range(n))

    # Start with the first node
    visited = {0}

    # Depth-first search to find all connected nodes
    stack = [0]
    while stack:
        node = stack.pop()
        for neighbor in range(n):
            if matrix[node][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
        to_visit.discard(node)

        # If all nodes have been visited, return True
        if not to_visit:
            return True

    return False