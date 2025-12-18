"""
QUESTION:
Implement a function `detectLoop` that takes as input a directed graph represented by an adjacency list `graph`, two boolean arrays `visited` and `checkedLoop`, and a vertex `u`. The function should return `True` if a loop is detected starting from vertex `u`, and `False` otherwise, using a depth-first search (DFS) approach and marking the vertices visited during the DFS in the `visited` array and the vertices in the loop in the `checkedLoop` array.
"""

def detectLoop(graph, visited, checkedLoop, u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            if detectLoop(graph, visited, checkedLoop, v):
                return True
        elif not checkedLoop[v]:
            return True

    checkedLoop[u] = True
    return False