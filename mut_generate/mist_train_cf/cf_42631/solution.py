"""
QUESTION:
Write a function `shortest_path(graph, start, target)` that takes a graph represented as a dictionary adjacency list, a start node, and a target node, and returns a list representing the shortest path from the start node to the target node. The graph dictionary keys are nodes, and values are lists of neighboring nodes. If there is no path from the start node to the target node, return an empty list.
"""

from collections import deque

def shortest_path(graph, start, target):
    if start not in graph or target not in graph:
        return []

    queue = deque([[start]])
    explored = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in explored:
            neighbors = graph[node]

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == target:
                    return new_path

            explored.add(node)

    return []