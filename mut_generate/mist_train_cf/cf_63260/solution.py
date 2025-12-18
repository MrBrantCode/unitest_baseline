"""
QUESTION:
Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is one where the height difference between the left and right subtrees of each node does not exceed 1. The quantity of nodes in the tree is between 0 and 5000, and the node values are between -10^4 and 10^4. Implement the function `isBalanced(root)` to return True if the tree is balanced and False otherwise.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isBalanced(root):
    def dfsHeight(root):
        if not root: 
            return 0
        leftHeight = dfsHeight(root.left)
        if leftHeight == -1: 
            return -1
        rightHeight = dfsHeight(root.right)
        if rightHeight == -1: 
            return -1
        if abs(leftHeight - rightHeight) > 1: 
            return -1
        return max(leftHeight, rightHeight) + 1

    return dfsHeight(root) != -1