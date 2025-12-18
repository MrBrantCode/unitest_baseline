"""
QUESTION:
Write a function called `is_balanced` that takes the root of a binary tree as input. The function should return `True` if the binary tree is balanced and `False` otherwise. A binary tree is considered balanced if the height of the two subtrees of any node never differ by more than 1. Assume the height of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(node):
    if node is None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    return max(left_height, right_height) + 1

def is_balanced(root):
    if root is None:
        return True
    left_height = height(root.left)
    right_height = height(root.right)
    if abs(left_height - right_height) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)