"""
QUESTION:
Implement a function named `BFS` that performs a Breadth-First Search traversal on a given tree. The tree is represented as an adjacency list, where each key is a node and its corresponding value is a list of neighboring nodes. The function should start the traversal from a specified root node and return a list of visited nodes. Assume the tree is an unweighted graph.
"""

from collections import deque

def BFS(tree, root):
    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        visited.append(node)

        for neighbour in tree[node]:
            if neighbour not in visited:
                queue.append(neighbour)

    return visited