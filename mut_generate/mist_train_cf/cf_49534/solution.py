"""
QUESTION:
Implement a function `hamiltonianCycleUntil` that checks if a Hamiltonian Cycle exists in a given graph using backtracking. The function should take a graph represented as an adjacency matrix, the current path as an array, and the current position in the path as parameters. The function should return `True` if a Hamiltonian Cycle is found and `False` otherwise. The graph has `V` vertices, and the path array is initially filled with `-1`. The function should also use a helper function `isSafe` to check if a vertex can be added to the current path.
"""

def isSafe(v, pos, path, graph):
    """
    Checks if a vertex can be added to the current path.

    Args:
    v (int): The vertex to be added.
    pos (int): The current position in the path.
    path (list): The current path.
    graph (list): The adjacency matrix of the graph.

    Returns:
    bool: True if the vertex can be added, False otherwise.
    """
    if graph[path[pos-1]][v] == 0:
        return False
    if v in path:
        return False
    return True

def hamiltonianCycleUntil(graph, path, pos):
    """
    Checks if a Hamiltonian Cycle exists in a given graph using backtracking.

    Args:
    graph (list): The adjacency matrix of the graph.
    path (list): The current path.
    pos (int): The current position in the path.

    Returns:
    bool: True if a Hamiltonian Cycle is found, False otherwise.
    """
    V = len(graph)
    if pos == V:
        return graph[path[pos-1]][path[0]] == 1
    for v in range(V):
        if isSafe(v, pos, path, graph):
            path[pos] = v
            if hamiltonianCycleUntil(graph, path, pos + 1):
                return True
            path[pos] = -1
    return False