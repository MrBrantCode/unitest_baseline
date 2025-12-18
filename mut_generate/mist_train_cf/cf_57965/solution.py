"""
QUESTION:
Implement a function named `BFS` that takes two parameters `start` and `end`, representing the starting and ending vertices in an unweighted graph. The function should return the shortest path between these two vertices using the Breadth-First Search algorithm. The graph is represented as an adjacency list, where each key is a vertex and its corresponding value is a list of its neighboring vertices.
"""

from collections import deque

def BFS(graph, start, end):
    """
    This function returns the shortest path between two vertices in an unweighted graph using the Breadth-First Search algorithm.

    Args:
    graph (dict): An adjacency list representing the graph.
    start (any): The starting vertex.
    end (any): The ending vertex.

    Returns:
    list: The shortest path from the start vertex to the end vertex. If there's no path, it returns None.
    """
    
    visited = {start}
    queue = deque([(start, [start])])

    while queue:
        vertex, path = queue.popleft()
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
            if neighbor == end:
                return path + [neighbor]
    return None