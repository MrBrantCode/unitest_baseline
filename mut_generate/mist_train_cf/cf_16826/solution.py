"""
QUESTION:
Write a function `maxPathSum` that takes the root of a binary tree as input and returns the maximum path sum, where the path must include the root node and at least one leaf node. 

The function should be able to handle binary trees where each node has a value and at most two children (left and right). The path sum is the sum of the values of all nodes in the path. The function should return the maximum possible path sum that meets the conditions.

The function should have a time complexity of O(N), where N is the number of nodes in the binary tree.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxPathSumHelper(node):
    if node is None:
        return 0, 0

    left_max_include, left_max_end = maxPathSumHelper(node.left)
    right_max_include, right_max_end = maxPathSumHelper(node.right)

    max_include = max(node.val + left_max_end + right_max_end,
                      left_max_include,
                      right_max_include)

    max_end = max(node.val + left_max_end,
                  node.val + right_max_end)

    return max_include, max_end

def maxPathSum(root):
    max_include, _ = maxPathSumHelper(root)
    return max_include