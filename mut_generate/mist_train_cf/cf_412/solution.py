"""
QUESTION:
Write a function `is_valid_bst` that checks if a given binary tree is a valid binary search tree and returns the number of leaf nodes in the binary tree. The function should have a time complexity of O(n log n) and a space complexity of O(log n). The function should take as input the root node of the binary tree and return a tuple containing a boolean indicating whether the binary tree is a valid binary search tree and the number of leaf nodes in the binary tree.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    """
    Checks if a given binary tree is a valid binary search tree and returns the number of leaf nodes in the binary tree.

    Args:
    root: The root node of the binary tree.
    min_val: The minimum allowed value for the current node (default is negative infinity).
    max_val: The maximum allowed value for the current node (default is positive infinity).

    Returns:
    A tuple containing a boolean indicating whether the binary tree is a valid binary search tree and the number of leaf nodes in the binary tree.
    """
    if root is None:
        return True, 0
    
    if not (min_val < root.val < max_val):
        return False, 0

    left_valid, left_leaf_count = is_valid_bst(root.left, min_val, root.val)
    if not left_valid:
        return False, 0

    right_valid, right_leaf_count = is_valid_bst(root.right, root.val, max_val)
    if not right_valid:
        return False, 0

    leaf_count = left_leaf_count + right_leaf_count
    if root.left is None and root.right is None:
        leaf_count += 1

    return True, leaf_count