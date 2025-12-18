"""
QUESTION:
Write a function `maxDepth` to calculate the maximum depth of a Binary Search Tree. The function takes the root of the Binary Search Tree as input and returns the maximum depth as an integer. The maximum depth of an empty tree is 0 and the depth of a tree with only one node is 1.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root):
    """
    Calculate the maximum depth of a Binary Search Tree.

    Args:
        root (TreeNode): The root of the Binary Search Tree.

    Returns:
        int: The maximum depth of the Binary Search Tree.
    """
    if root is None:
        return 0
    else:
        return max(maxDepth(root.left), maxDepth(root.right)) + 1