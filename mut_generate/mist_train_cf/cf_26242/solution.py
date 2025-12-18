"""
QUESTION:
Write a function `printLevelOrder` that, given the root of a binary tree, prints all elements level by level from top to bottom and left to right.
"""

from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelOrder(root):
    """
    Prints all elements of a binary tree level by level from top to bottom and left to right.

    Args:
    root (TreeNode): The root of the binary tree.
    """
    if root is None:
        return

    queue = deque([root])

    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            print(node.data, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()  # New line after each level