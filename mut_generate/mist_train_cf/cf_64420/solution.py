"""
QUESTION:
Implement a function `maxDepth(root)` that takes the root of a binary tree as input, where each node in the tree has a `val`, `left`, and `right` attribute, and returns the maximum depth or height of the tree. The function should handle the case where the tree is empty (i.e., the root is `None`).
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root: TreeNode) -> int:
    if not root: 
        return 0 
    else:
        left_height = maxDepth(root.left)
        right_height = maxDepth(root.right)
        return max(left_height, right_height) + 1