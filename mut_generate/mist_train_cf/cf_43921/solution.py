"""
QUESTION:
Implement a function `BFS` in Python that performs a breadth-first search on an unweighted graph. The function should take a graph represented as an adjacency list and a starting vertex as input, and it should return a list of vertices in the order they were visited. Assume the graph is represented as a dictionary where each key is a vertex and its corresponding value is a list of its neighbors. The function should not use any external libraries.
"""

from collections import deque

def BFS(graph, start):
    """
    Performs a breadth-first search on an unweighted graph.

    Args:
    graph (dict): A dictionary representing the graph, where each key is a vertex and its corresponding value is a list of its neighbors.
    start (any): The starting vertex for the search.

    Returns:
    list: A list of vertices in the order they were visited.
    """
    visited = set()
    visited_order = []
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        visited_order.append(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return visited_order