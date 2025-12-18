"""
QUESTION:
Write a function `maxDepth` that calculates the maximum depth of a binary tree. The function takes the root node of the binary tree as input and returns the maximum depth as an integer. If the tree is empty (i.e., the root is `None`), the function should return 0.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root):
    """
    Calculate the maximum depth of a binary tree.

    Args:
    root (TreeNode): The root node of the binary tree.

    Returns:
    int: The maximum depth of the binary tree.
    """
    # Base case
    if root is None:
        return 0
    
    # Recur for left subtree and right subtree
    lDepth = maxDepth(root.left)
    rDepth = maxDepth(root.right)
    
    # Use the larger one
    return max(lDepth, rDepth) + 1