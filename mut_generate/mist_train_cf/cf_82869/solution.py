"""
QUESTION:
Write a function `isBalanced` to check if a given binary tree is balanced. A binary tree is balanced if the difference between the height of the left subtree and right subtree is no more than 1, and both the left subtree and right subtree are balanced. The function should return `True` if the binary tree is balanced and `False` otherwise.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isBalanced(root):
    """
    Checks if a binary tree is balanced.
    
    A binary tree is balanced if the difference between the height of the left subtree 
    and right subtree is no more than 1, and both the left subtree and right subtree are balanced.
    
    Args:
    root (TreeNode): The root of the binary tree.
    
    Returns:
    bool: True if the binary tree is balanced, False otherwise.
    """

    def height(node):
        """
        Computes the height of the tree.
        
        Args:
        node (TreeNode): The root of the subtree.
        
        Returns:
        int: The height of the subtree.
        """
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))

    if not root:
        return True
    left_height = height(root.left)
    right_height = height(root.right)
    if abs(left_height - right_height) > 1:
        return False
    return isBalanced(root.left) and isBalanced(root.right)