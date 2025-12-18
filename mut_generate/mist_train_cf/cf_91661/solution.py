"""
QUESTION:
Write a recursive function called `dfs_binary_tree` that performs a depth-first search on a binary tree and returns a list of node values in the order they were visited. The binary tree is represented by nodes with a `value`, `left` child, and `right` child.
"""

def dfs_binary_tree(node):
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    visited = []
    if node:
        visited.append(node.value)
        visited += dfs_binary_tree(node.left)
        visited += dfs_binary_tree(node.right)
    return visited