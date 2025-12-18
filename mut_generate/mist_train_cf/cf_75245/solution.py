"""
QUESTION:
Create a function named `PreorderTraversal` that performs a pre-order depth-first traversal on a binary tree. The function should take a binary tree node as input and return a list of node values in the order they are visited. The function should handle the possibility of both left and right subtree traversals. The binary tree node structure is defined by the Node class with `data`, `left`, and `right` attributes.
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def PreorderTraversal(root):
    res = []
    if root:
        res.append(root.data)
        res = res + PreorderTraversal(root.left)
        res = res + PreorderTraversal(root.right)
    return res