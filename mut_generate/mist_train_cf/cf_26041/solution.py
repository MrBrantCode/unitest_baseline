"""
QUESTION:
Create a function called `levelOrder` that takes the root of a binary tree as input and prints the values of its nodes level by level, starting from the root level. The binary tree node structure has an integer `data` field and pointers to its `left` and `right` children.
"""

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelOrder(root):
    """
    Prints the values of a binary tree's nodes level by level, starting from the root level.

    Args:
    root (Node): The root of the binary tree.
    """
    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.data, end=" ")

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)