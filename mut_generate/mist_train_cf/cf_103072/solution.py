"""
QUESTION:
Design a function `find_min_max` that takes a collection of numbers as input and returns the minimum and maximum elements with a time complexity of O(log n).
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_min_max(root):
    """
    Find the minimum and maximum elements in a binary search tree.

    Args:
    root (Node): The root of the binary search tree.

    Returns:
    tuple: A tuple containing the minimum and maximum elements.
    """

    # Base case: If the tree is empty, return None for both min and max
    if root is None:
        return None, None

    # Find the minimum element by traversing to the leftmost leaf node
    min_node = root
    while min_node.left:
        min_node = min_node.left
    min_val = min_node.val

    # Find the maximum element by traversing to the rightmost leaf node
    max_node = root
    while max_node.right:
        max_node = max_node.right
    max_val = max_node.val

    return min_val, max_val