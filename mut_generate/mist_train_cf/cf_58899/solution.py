"""
QUESTION:
Implement a function `compute_height(node)` that calculates the dimensional magnitude (height) of a binary tree given its root node, handling empty nodes and exceptions. The function should return the height of the binary tree.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def compute_height(node):
    # Function that computes the height of the binary tree.
    if node is None:
        return 0

    return max(compute_height(node.left), compute_height(node.right)) + 1