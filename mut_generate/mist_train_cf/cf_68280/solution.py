"""
QUESTION:
Create a function `insert` to construct a binary search tree from a given pre-order traversal sequence, ensuring each node follows the binary search tree properties. The function should take a node and a key as input and return the updated node. The binary search tree properties state that for any given node, the value of all nodes in its left sub-tree is less than the value of the given node, and the value of all nodes in its right sub-tree is greater.
"""

class Node:
    def __init__(self, key):
        self.key = key 
        self.left = None
        self.right = None

def insert(node, key):
    if node is None:
        return Node(key)
    else:
        if node.key < key:
            node.right = insert(node.right, key)
        else:
            node.left = insert(node.left, key)
    return node