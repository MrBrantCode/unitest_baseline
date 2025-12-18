"""
QUESTION:
Implement a priority queue using a binary search tree with the Lowest-Value-In, Highest-Priority-Out principle, where items with lower values have higher priority. The binary search tree should maintain the Left-Smaller-Right-Larger property, where every node has a value larger or equal to each node in its left subtree and smaller than each node in its right subtree.

Design an algorithm with the following functions: `insert(value)` to add a new item to the priority queue, and `remove_highest_priority()` to remove and return the item with the highest priority (smallest value). Ensure the time complexity for insertion and removal operations is O(logN) in the average case, and handle cases where the tree becomes unbalanced.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def entrant(value, root=None):
    """
    Inserts a new item into the priority queue (BST).

    Args:
    value: The value of the item to be inserted.
    root: The current root of the BST (default is None).

    Returns:
    The updated root of the BST.
    """
    if root is None:
        return Node(value)
    elif value < root.value:
        root.left = entrant(value, root.left)
    else:
        root.right = entrant(value, root.right)
    return root

def remove_highest_priority(root):
    """
    Removes and returns the item with the highest priority (smallest value) from the priority queue (BST).

    Args:
    root: The current root of the BST.

    Returns:
    A tuple containing the value of the removed item and the updated root of the BST.
    """
    if root is None:
        return None, None
    elif root.left is None:
        return root.value, root.right
    else:
        value, root.left = remove_highest_priority(root.left)
        return value, root