"""
QUESTION:
Write a function named `BFS_shortest_path` that determines the shortest path between two nodes in an unweighted, unsorted binary tree using Breadth-First Search. The function should take three parameters: a dictionary representing the binary tree where the keys are node values and the values are lists of connected nodes, and two node values representing the start and goal nodes. The function should return a list of node values representing the shortest path from the start node to the goal node. If no path exists, the function should return `None`.
"""

from collections import deque

def BFS_shortest_path(tree, start, goal):
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for next_node in tree.get(node, []):
            new_path = list(path)
            new_path.append(next_node)
            queue.append(new_path)
    return None