"""
QUESTION:
Create a function `is_bst` that takes the root of a binary tree as input and returns a boolean indicating whether the binary tree is a valid binary search tree. The function should work for any binary tree, not just those created from a sorted list. A binary search tree is valid if for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The function should handle the case where the input tree is empty (i.e., its root is None).
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def is_bst(node, min=float("-inf"), max=float("inf")):
    """
    Checks if a binary tree rooted at 'node' is a binary search tree.

    Args:
        node: The root node of the binary tree.
        min: The minimum allowed value for the node's data (default: negative infinity).
        max: The maximum allowed value for the node's data (default: positive infinity).

    Returns:
        True if the binary tree is a valid binary search tree, False otherwise.
    """
    if not node:
        return True
    if node.data < min or node.data > max:
        return False
    return (is_bst(node.left, min, node.data - 1) and 
            is_bst(node.right, node.data + 1, max))