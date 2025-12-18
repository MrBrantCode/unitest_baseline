"""
QUESTION:
Construct a Python function `maxDiff(root, target)` that takes the root of a binary search tree and a target value as input, and returns the node value in the tree with the minimum absolute difference to the target. The function should utilize the properties of the binary search tree to minimize the numerical difference between the nearby nodes and the target value.
"""

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def maxDiff(root, target):
    target_node = None
    min_diff = float('inf')

    while root:
        if root.val == target:
            return root.val
        if abs(root.val - target) < min_diff:
            min_diff = abs(root.val - target)
            target_node = root.val
        if target < root.val:
            root = root.left
        else:
            root = root.right

    return target_node