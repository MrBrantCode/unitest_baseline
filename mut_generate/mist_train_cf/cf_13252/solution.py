"""
QUESTION:
Write a function named `bfs_traversal` that takes the root of a binary tree as input and returns a list of node values in the order they are visited using breadth-first search (BFS) traversal. The binary tree nodes are defined as objects with `val`, `left`, and `right` attributes. Assume that the input binary tree is represented using a `TreeNode` class.
"""

from collections import deque

def bfs_traversal(root):
    if root is None:
        return []

    result = []
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result