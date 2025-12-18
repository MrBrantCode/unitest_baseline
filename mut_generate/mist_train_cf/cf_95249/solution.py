"""
QUESTION:
Create a function named `count_leaf_nodes` that calculates the number of leaf nodes in a binary tree with a time complexity of O(log n), where n is the number of nodes in the binary tree. The binary tree is defined by a Node class with a value, left child, and right child. The function should return the total count of leaf nodes in the binary tree.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_leaf_nodes(root):
    leafCount = 0

    def dfs(node):
        nonlocal leafCount
        if node is None:
            return
        if node.left is None and node.right is None:
            leafCount += 1
        if node.left:
            dfs(node.left)
        if node.right:
            dfs(node.right)

    dfs(root)
    return leafCount