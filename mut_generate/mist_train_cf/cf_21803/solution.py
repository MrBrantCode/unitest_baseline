"""
QUESTION:
Write a function named `is_balanced` that takes the root of a binary tree as input and returns True if the binary tree is balanced and False otherwise. A binary tree is balanced if the heights of the two subtrees of any node never differ by more than 1. The height of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    def get_height(node):
        if node is None:
            return 0
        return 1 + max(get_height(node.left), get_height(node.right))

    if root is None:
        return True
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    if abs(left_height - right_height) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)