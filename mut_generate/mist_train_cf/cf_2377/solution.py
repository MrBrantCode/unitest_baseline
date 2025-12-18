"""
QUESTION:
Implement a breadth-first search function called `breadth_first_search` that takes a directed graph, a start vertex, and an end vertex as input. The function should return the shortest path from the start vertex to the end vertex in the graph. The space complexity should be O(n) and the time complexity should be O(V+E), where V is the number of vertices and E is the number of edges in the graph.
"""

from collections import deque

def breadth_first_search(graph, start, end):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        vertex, path = queue.popleft()

        if vertex == end:
            return path

        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                queue.append((neighbor, path + [neighbor]))

    return None