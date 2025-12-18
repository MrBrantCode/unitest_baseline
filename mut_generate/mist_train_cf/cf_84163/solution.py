"""
QUESTION:
Write a recursive function `find_max` to find the maximum number in a given list of integers. The function should handle the case where the list is empty. Additionally, write a recursive function `maxPathSum` to find the maximum sum of all possible paths from the root node to the leaves in a binary tree. Define a class `TreeNode` for the binary tree nodes.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxPathSum(root):
    max_path=[float('-inf')]
    def helper(node):
        if not node:
            return 0
        left = max(helper(node.left), 0)
        right = max(helper(node.right), 0)
        max_path[0] = max(max_path[0], left+right+node.val)
        return max(left, right)+node.val
    helper(root)
    return max_path[0]