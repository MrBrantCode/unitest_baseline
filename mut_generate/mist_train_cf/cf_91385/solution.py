"""
QUESTION:
Write a function `is_identical(node1, node2)` that checks if two binary tree structures are identical at all levels. The function should take two tree nodes as parameters and return `True` if the trees are identical, and `False` otherwise. The function should handle the case where the trees are empty (i.e., both `node1` and `node2` are `None`).
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_identical(node1, node2):
    # Base case: both nodes are None
    if node1 is None and node2 is None:
        return True

    # Base case: one of the nodes is None, or their values are different
    if node1 is None or node2 is None or node1.value != node2.value:
        return False

    # Recursively check left and right subtrees
    left_identical = is_identical(node1.left, node2.left)
    right_identical = is_identical(node1.right, node2.right)

    # Return True if both subtrees are identical
    return left_identical and right_identical