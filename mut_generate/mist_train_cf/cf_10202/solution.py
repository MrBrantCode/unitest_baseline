"""
QUESTION:
Write a function `maxPathSum` that takes the root of a binary tree as input and returns the maximum path sum where the path must include the root node and at least one leaf node.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def maxPathSum(root):
    def maxPathSumHelper(node):
        if node is None:
            return 0

        leftSum = maxPathSumHelper(node.left)
        rightSum = maxPathSumHelper(node.right)

        maxSum = max(node.value, node.value + max(leftSum, rightSum))

        return max(maxSum, leftSum, rightSum)

    return maxPathSumHelper(root)