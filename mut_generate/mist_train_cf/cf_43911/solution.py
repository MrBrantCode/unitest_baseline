"""
QUESTION:
Given a binary tree, write a function called `find_deepest_node` that calculates the maximum depth of the tree and identifies the exact node at the maximum depth. The function should return this node and its depth. The function should operate in O(n) time complexity. Note that O(1) space complexity may not be achievable due to the need to traverse each node.
"""

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def find_deepest_node(root, level=0, max_=float('-inf'), node=None):
    if root is None:
        return max_, node
    if level > max_:
        max_ = level
        node = root
    max_, node = find_deepest_node(root.left, level+1, max_, node)
    max_, node = find_deepest_node(root.right, level+1, max_, node)
    return max_, node