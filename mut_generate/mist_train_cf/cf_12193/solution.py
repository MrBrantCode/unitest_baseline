"""
QUESTION:
Create a function `maxDepth` to compute the depth of a binary tree with a time complexity of O(n), where n is the number of nodes in the tree. The function should take the root of the binary tree as input and return the depth of the tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if root is None:
        return 0
    
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    return max(left_depth, right_depth) + 1