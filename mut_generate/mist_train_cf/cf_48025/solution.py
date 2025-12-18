"""
QUESTION:
Create a function called `solve` that takes the root of a binary tree as input. The function should return the longest path from the root to the deepest leaf node if the tree is univalued (all nodes have the same value), and -1 otherwise. The function should return the depth of the tree (the number of nodes from the root to the deepest leaf node) as the longest path.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    def isUnivalued(node):
        if not node:
            return True
        if node.left and node.val != node.left.val:
            return False
        if node.right and node.val != node.right.val:
            return False
        return isUnivalued(node.left) and isUnivalued(node.right)

    def getDepth(node):
        if not node:
            return 0
        return 1 + max(getDepth(node.left), getDepth(node.right))

    if isUnivalued(root):
        return getDepth(root)
    return -1