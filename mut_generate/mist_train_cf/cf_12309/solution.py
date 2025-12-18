"""
QUESTION:
Write a function `binary_search_tree_search` that searches for a target element in a binary search tree. The function should have a time complexity of less than O(log n) if possible. The function should take in the root of the binary search tree and the target element as input, and return the target element if found, or None otherwise. Assume the binary search tree node has an integer value, a left child, and a right child.
"""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def binary_search_tree_search(root, target):
    if root is None:
        return None
    if root.value == target:
        return root
    elif root.value < target:
        return binary_search_tree_search(root.right, target)
    else:
        return binary_search_tree_search(root.left, target)