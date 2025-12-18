"""
QUESTION:
Design a function called `find_LCA` to find the lowest common ancestor (LCA) of two nodes `n1` and `n2` in a binary tree. The function should take the root of the binary tree and the values of `n1` and `n2` as input and return the node that is the LCA of `n1` and `n2`. The binary tree may or may not be a binary search tree, and it may contain duplicate values.
"""

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def find_LCA(root, n1, n2):
    while root:
        if root.data > n1 and root.data > n2:
            root = root.left
        elif root.data < n1 and root.data < n2:
            root = root.right
        else: 
            break
    return root 