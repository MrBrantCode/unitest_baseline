"""
QUESTION:
Write a function sumOfLeftLeaves that calculates the cumulative total of all left leaves present in a specified binary tree. The function should take the root of the binary tree as input and return the sum of the values of the left leaves. The function may be recursive or iterative. The binary tree node is defined as a class with a value and optional left and right children.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root, is_left=False):
    if not root:
        return 0
    if not root.left and not root.right and is_left:
        return root.val
    return sumOfLeftLeaves(root.left, True) + sumOfLeftLeaves(root.right, False)