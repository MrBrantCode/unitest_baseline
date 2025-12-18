"""
QUESTION:
Create a function named `max_depth` that takes a binary tree root node as input and returns the depth of the tree. The function should have a time complexity of O(n), where n is the number of nodes in the tree, and use constant space.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def entance(root):
    if root is None:
        return 0
    else:
        left_depth = entance(root.left)
        right_depth = entance(root.right)
        return max(left_depth, right_depth) + 1