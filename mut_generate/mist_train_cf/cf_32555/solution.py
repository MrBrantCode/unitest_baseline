"""
QUESTION:
Implement a Python class `Node` to represent a node in a binary tree with attributes `data`, `left`, and `right`. The `data` attribute represents the node's value, while `left` and `right` represent the left and right child nodes, initialized to `None` by default. Then, implement a function `sizeTree(node)` that calculates the size of the binary tree, defined as the total number of nodes in the tree, by recursively counting the nodes in the left and right subtrees and adding 1 for the current node. If the input node is `None`, the function should return 0.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sizeTree(node):
    if node is None:
        return 0
    else:
        return (sizeTree(node.left) + 1 + sizeTree(node.right))