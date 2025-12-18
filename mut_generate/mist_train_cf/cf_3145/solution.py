"""
QUESTION:
Implement a function, `find_min_max`, that uses a binary search tree (BST) to find the minimum and maximum elements from a collection of numbers. The function should have a time complexity of O(log n) and be able to handle negative numbers efficiently. The implementation should not use any built-in data structures or libraries such as arrays, lists, or heaps.
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
    tuple: A tuple containing the minimum and maximum elements in the binary search tree.
    """
    if root is None:
        return None, None

    min_val = root.val
    max_val = root.val

    # Find the minimum element
    node = root
    while node.left:
        node = node.left
        min_val = node.val

    # Find the maximum element
    node = root
    while node.right:
        node = node.right
        max_val = node.val

    return min_val, max_val