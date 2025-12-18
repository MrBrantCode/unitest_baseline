"""
QUESTION:
Implement a breadth-first search function `breadth_first_search` that takes a graph and two vertices `start` and `end` as input. The function should return the shortest path between `start` and `end` in the graph. The graph can be directed, and the function should have a space complexity of O(n) and a time complexity of O(V+E), where V is the number of vertices and E is the number of edges.
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