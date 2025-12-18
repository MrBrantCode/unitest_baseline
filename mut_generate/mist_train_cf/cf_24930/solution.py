"""
QUESTION:
Write a function named `search_bst` to find a target element in a binary search tree. The function should take the root of the binary search tree and the target element as input and return the target node if found, or None otherwise. The time complexity of the function should be less than O(n), where n is the number of nodes in the binary search tree.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def search_bst(root, target):
    """
    Searches for a target element in a binary search tree.

    Args:
    root (TreeNode): The root of the binary search tree.
    target (int): The target element to be searched.

    Returns:
    TreeNode: The target node if found, or None otherwise.
    """
    if root is None or root.val == target:
        return root
    if target < root.val:
        return search_bst(root.left, target)
    return search_bst(root.right, target)