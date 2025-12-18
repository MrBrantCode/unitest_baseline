"""
QUESTION:
Write a function `countLeafNodes` to count the number of leaf nodes in a binary tree represented as a nested dictionary. A leaf node is a node with no children (i.e., both "left" and "right" keys are `None`). The function should recursively traverse the tree and return the total count of leaf nodes. The binary tree is represented as a dictionary with "data", "left", and "right" keys, where "left" and "right" keys hold the left and right child nodes respectively, or `None` if the node is a leaf node.
"""

def countLeafNodes(tree):
    if tree is None:
        return 0
    if tree["left"] is None and tree["right"] is None:
        return 1 
    leftLeaf = countLeafNodes(tree["left"])
    rightLeaf = countLeafNodes(tree["right"])
    return leftLeaf + rightLeaf