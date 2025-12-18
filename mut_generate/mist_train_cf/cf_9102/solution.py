"""
QUESTION:
Write a function `sum_of_nodes` to find the sum of all the nodes in a binary tree. The function should take the root node of the binary tree as input and return the total sum of all node values. The function must use recursion.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_of_nodes(root):
    if root is None:
        return 0
    return root.val + sum_of_nodes(root.left) + sum_of_nodes(root.right)