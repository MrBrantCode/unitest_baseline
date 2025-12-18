"""
QUESTION:
Write a function `find_lca(root, node1, node2)` that finds the least common ancestor of two given nodes `node1` and `node2` in a binary search tree rooted at `node`. Each node in the tree has a unique integer key. The key of each node is greater than the keys of all nodes in its left subtree and less than the keys of all nodes in its right subtree. Assume both `node1` and `node2` exist in the binary search tree.
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_lca(root, node1, node2):
    if root is None:
        return None

    # If both nodes are less than the root, move to the left child
    if node1 < root.key and node2 < root.key:
        return find_lca(root.left, node1, node2)
    
    # If both nodes are greater than the root, move to the right child
    if node1 > root.key and node2 > root.key:
        return find_lca(root.right, node1, node2)

    # If one node is less than the root and the other is greater, or if one node is equal to the root,
    # then the root is the LCA
    return root.key