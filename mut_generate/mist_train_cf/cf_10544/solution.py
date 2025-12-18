"""
QUESTION:
Implement a function `bfs` that performs a breadth-first search in a directed graph. The function should take as input a graph represented as a dictionary where the keys are the vertices and the values are lists of adjacent vertices, as well as a start vertex and an end vertex. It should return the shortest path between the start vertex and the end vertex. The function should have a time complexity of O(V+E), where V is the number of vertices and E is the number of edges, and a space complexity of O(n), where n is the number of vertices. If no path exists, the function should return None.
"""

from collections import deque

def bfs(graph, start, end):
    # Create a queue for BFS and enqueue the start vertex
    queue = deque([(start, [start])])

    # Keep track of visited vertices
    visited = set()

    # Perform BFS
    while queue:
        vertex, path = queue.popleft()
        visited.add(vertex)

        # Check if we have reached the destination vertex
        if vertex == end:
            return path

        # Enqueue adjacent vertices
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

    # If no path is found, return None
    return None