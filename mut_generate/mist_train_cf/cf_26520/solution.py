"""
QUESTION:
Implement the `insert` method in the `BinarySearchTree` class. The `insert` method should take two parameters: `node` (the current node in the tree) and `data` (the value to be inserted). The method should insert the `data` into the binary search tree while maintaining the binary search tree property. If `node` is `None`, create a new node with the given `data`. If `data` is less than the `node`'s `data`, insert `data` into the left subtree; otherwise, insert `data` into the right subtree. The method should return the modified `node`.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(node, data):
    """
    Insert a new node with the given data into the binary search tree.
    """
    if node is None:
        return Node(data)
    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)
    return node