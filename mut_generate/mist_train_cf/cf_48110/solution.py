"""
QUESTION:
Create a function named `insert` to create a binary search tree (BST) from a list of numbers using a modification of the insertion sort algorithm that handles duplicate nodes. The function should take two parameters: `root` (the root node of the BST) and `data` (the number to be inserted into the BST). The function should return the root node of the updated BST. The BST should not contain any duplicate nodes.
"""

def insert(root, data):
    """
    Insert a node into a binary search tree (BST) and handle duplicate nodes.

    Parameters:
    root (Node): The root node of the BST.
    data (int): The number to be inserted into the BST.

    Returns:
    Node: The root node of the updated BST.
    """
    if root is None:
        return Node(data)
    else:
        if data > root.data:
            if root.right is None:
                root.right = Node(data)
            else:
                insert(root.right, data)
        elif data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                insert(root.left, data)
    return root

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None