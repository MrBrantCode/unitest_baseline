"""
QUESTION:
Write a function `max_path_sum` that takes the root of a binary tree as input and returns the maximum path sum within the tree, where a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections, and the path must contain at least one node but does not need to go through the root.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root: TreeNode) -> int:
    max_sum = float('-inf')

    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        path_sum = node.val + left_gain + right_gain
        max_sum = max(max_sum, path_sum)
        return node.val + max(left_gain, right_gain)

    max_gain(root)
    return max_sum