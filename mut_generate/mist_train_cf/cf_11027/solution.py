"""
QUESTION:
Implement the function `bfs_with_shortest_path` that performs a breadth-first search (BFS) on a graph and returns a dictionary where the keys are nodes and the values are the shortest paths from the starting node to each node. The graph is represented as a dictionary where each node is a key, and its neighbors are values stored as lists.
"""

from collections import deque

def bfs_with_shortest_path(graph, start):
    queue = deque()
    visited = set()
    queue.append(start)
    shortest_paths = {start: [start]}

    while queue:
        node = queue.popleft()
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                shortest_paths[neighbor] = shortest_paths[node] + [neighbor]

    return shortest_paths