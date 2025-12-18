"""
QUESTION:
Design a function named "isIdenticalAndMirrored" that takes two binary tree nodes as parameters and returns a boolean indicating if the trees rooted at those nodes are identical at all levels and mirror images. The binary trees are also binary search trees and the values in the nodes are floating-point numbers. The function should handle the base case where both nodes are null and return true, and the case where only one of the nodes is null and return false.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def isIdenticalAndMirrored(node1, node2):
    def isIdentical(node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.value != node2.value:
            return False
        return isIdentical(node1.left, node2.left) and isIdentical(node1.right, node2.right)

    def isMirrored(node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.value != node2.value:
            return False
        return isMirrored(node1.left, node2.right) and isMirrored(node1.right, node2.left)

    if not isIdentical(node1, node2):
        return False
    return isMirrored(node1, node2)