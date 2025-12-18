"""
QUESTION:
Implement a binary search tree with a search function named `search(node, item)` that searches for a given item in the tree. The binary search tree should follow the property where all elements in the left subtree of a node are less than the node's value and all elements in the right subtree are greater. The function should return the node if the item is found, and `None` otherwise.
"""

class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None

def search(node, item):
    if node is None or node.val == item:
        return node
    if node.val < item:
        return search(node.right, item)
    return search(node.left, item)