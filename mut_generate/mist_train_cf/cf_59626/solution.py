"""
QUESTION:
Write a function `maxDepth` that calculates the maximum depth of a given binary tree. The binary tree is represented by a `TreeNode` class with `value`, `left`, and `right` attributes. The function should take the `root` of the binary tree as input and return the maximum depth as an integer. If the binary tree is empty (i.e., `root` is `None`), the function should return 0.
"""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def maxDepth(root):
    if root is None:
        return 0
    else:
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)

        return max(left_depth, right_depth) + 1