"""
QUESTION:
Implement a function `bfs(graph, start, end)` that performs a breadth-first search on a directed graph to find the shortest path between two given vertices. The function should have a space complexity of O(n) and a time complexity of O(V+E), where V is the number of vertices and E is the number of edges in the graph. The graph should be represented as an adjacency list, where each key is a vertex and its corresponding value is a list of neighboring vertices.
"""

from collections import deque

def bfs(graph, start, end):
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)
    parent = {}  

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

    return None 