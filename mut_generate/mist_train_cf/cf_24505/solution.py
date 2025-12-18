"""
QUESTION:
Write a function `count_nodes` that takes the root of a binary tree as input and returns the number of nodes in the binary tree. The binary tree is defined by a node class with a value and left and right child nodes. The function should be able to handle an empty tree, in which case it should return 0.
"""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def count_nodes(root):
    """
    Counts the number of nodes in a binary tree.

    Args:
    root: The root node of the binary tree.

    Returns:
    An integer representing the number of nodes in the binary tree.
    """
    if root is None:
        return 0
    else:
        return 1 + count_nodes(root.left) + count_nodes(root.right)