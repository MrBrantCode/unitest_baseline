"""
QUESTION:
Write a function named `is_valid_bst` that checks whether a given binary tree is a valid binary search tree and returns the number of nodes in the binary tree. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of nodes in the binary tree. The binary tree is represented using nodes with a `value`, `left` child, and `right` child. The function should return a boolean indicating whether the binary tree is valid and an integer representing the number of nodes.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_valid_bst(root, min_value=float('-inf'), max_value=float('inf')):
    """
    Checks whether a given binary tree is a valid binary search tree and returns the number of nodes in the binary tree.
    
    Args:
    root: The root node of the binary tree.
    min_value: The minimum allowed value for the current node (default is negative infinity).
    max_value: The maximum allowed value for the current node (default is positive infinity).
    
    Returns:
    A tuple containing a boolean indicating whether the binary tree is valid and an integer representing the number of nodes.
    """
    
    # Base case: An empty tree is a valid BST with 0 nodes
    if root is None:
        return True, 0
    
    # Check if the current node's value is within the allowed range
    if not min_value < root.value < max_value:
        return False, 0
    
    # Recursively check the left and right subtrees
    is_valid_left, num_nodes_left = is_valid_bst(root.left, min_value, root.value)
    is_valid_right, num_nodes_right = is_valid_bst(root.right, root.value, max_value)
    
    # If either subtree is not valid, the entire tree is not valid
    if not is_valid_left or not is_valid_right:
        return False, 0
    
    # The total number of nodes is 1 (the current node) plus the nodes in the left and right subtrees
    return True, 1 + num_nodes_left + num_nodes_right