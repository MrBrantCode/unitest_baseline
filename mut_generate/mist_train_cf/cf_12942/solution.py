"""
QUESTION:
Construct a function named `bstFromPreorder` that takes an array of integers representing a pre-order traversal sequence of a binary tree and returns the root of the constructed binary search tree. The binary search tree should satisfy the property that each node's value is greater than all the values in its left subtree and less than all the values in its right subtree.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def bstFromPreorder(preorder):
    def helper(lower, upper):
        if not preorder or preorder[0] < lower or preorder[0] > upper:
            return None
        root = TreeNode(preorder.pop(0))
        root.left = helper(lower, root.val)
        root.right = helper(root.val, upper)
        return root
    
    return helper(float('-inf'), float('inf'))