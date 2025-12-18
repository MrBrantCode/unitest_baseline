"""
QUESTION:
Write a function called `binaryTreeToArray` that takes the root node of a binary tree as input and returns a list of node values in the order they are visited using in-order traversal (left-node-right). The function should handle trees of any size and structure, and should not require any additional inputs besides the root node.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def binaryTreeToArray(root, array=None):
    if array is None:
        array = []
    if root:
        binaryTreeToArray(root.left, array)
        array.append(root.val)
        binaryTreeToArray(root.right, array)
    return array