"""
QUESTION:
Create a function `maxDepth(node)` that calculates the depth of a binary tree given its root node. The function should return the maximum depth of the binary tree, considering the depth of the tree to be the number of nodes along the longest path from the root node down to the farthest leaf node. The function should handle cases where the tree is empty (i.e., the root node is `None`).
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def maxDepth(node):
    if node is None:
        return 0 
    else:
        left_depth = maxDepth(node.left)
        right_depth = maxDepth(node.right)
        if (left_depth > right_depth):
            return left_depth+1
        else:
            return right_depth+1