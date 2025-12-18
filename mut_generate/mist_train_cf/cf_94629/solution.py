"""
QUESTION:
Implement a function `bfs` that performs a breadth-first search on a directed graph. The function should have a space complexity of O(n), where n is the number of vertices in the graph, and a time complexity of O(V+E), where V is the number of vertices and E is the number of edges in the graph. The function should take as input a dictionary representing the adjacency list of the graph, a start vertex, and an end vertex. It should return the shortest path from the start vertex to the end vertex if such a path exists, or None otherwise.
"""

from collections import deque

def bfs(graph, start, end):
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)
    parent = {}  # To keep track of the parent node for each visited node

    while queue:
        node = queue.popleft()
        if node == end:
            path = []
            while node != start:
                path.append(node)
                node = parent[node]
            path.append(start)
            path.reverse()
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = node

    return None  # If there's no path between start and end