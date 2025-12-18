"""
QUESTION:
Write a function called `get_root_and_sum` that takes the root of a binary tree as input and returns a tuple containing the root and the sum of all node values in the tree. The binary tree nodes are represented as objects with `val`, `left`, and `right` attributes.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_root_and_sum(root):
    if root is None:
        return None, 0
    else:
        left_root, left_sum = get_root_and_sum(root.left)
        right_root, right_sum = get_root_and_sum(root.right)
        total_sum = root.val + left_sum + right_sum
        return root, total_sum