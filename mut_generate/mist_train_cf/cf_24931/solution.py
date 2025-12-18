"""
QUESTION:
Design a function `is_identical` that checks if two given binary trees are identical. The function should take the roots of the two binary trees as input and return `True` if the trees are identical, and `False` otherwise. The function should not assume any specific structure or values of the binary trees.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_identical(root1, root2):
    """
    Checks if two given binary trees are identical.

    Args:
    root1 (TreeNode): The root of the first binary tree.
    root2 (TreeNode): The root of the second binary tree.

    Returns:
    bool: True if the two binary trees are identical, False otherwise.
    """
    # If both trees are empty, they are identical
    if root1 is None and root2 is None:
        return True
    
    # If one tree is empty and the other is not, they are not identical
    if root1 is None or root2 is None:
        return False
    
    # If the values of the root nodes are different, the trees are not identical
    if root1.val != root2.val:
        return False
    
    # Recursively check the left and right subtrees
    return is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)