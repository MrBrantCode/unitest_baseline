"""
QUESTION:
Design a function `closestValue` that takes the `root` of a binary search tree and a `target` value as input and returns the value within the BST that is closest to the `target`. The function should work for binary search trees with 1 to 10^4 nodes, and node values and target values ranging from 0 to 10^9.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def closestValue(root, target):
    def closestValueHelper(root, target, closest):
        if root is None:
            return closest
        if abs(target - closest) > abs(target - root.val):
            closest = root.val
        if target < root.val:
            return closestValueHelper(root.left, target, closest)
        elif target > root.val:
            return closestValueHelper(root.right, target, closest)
        else:
            return closest
    return closestValueHelper(root, target, float('inf'))