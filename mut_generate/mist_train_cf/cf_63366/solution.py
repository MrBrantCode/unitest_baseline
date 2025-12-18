"""
QUESTION:
Create a function `insert` that inserts a value into a binary search tree (BST) while maintaining the BST properties. Then, create a function `preorder` that performs a pre-order traversal of the BST and prints the node values in ascending order. Given a sequence of unique numbers, use these functions to insert the numbers into the BST and return the pre-order traversal of the sorted elements.
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    """
    Inserts a value into a binary search tree (BST) while maintaining the BST properties.
    
    Args:
    root (Node): The root of the BST.
    key (int): The value to be inserted.
    
    Returns:
    Node: The root of the updated BST.
    """
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def preorder(root):
    """
    Performs a pre-order traversal of the BST and prints the node values in ascending order.
    
    Args:
    root (Node): The root of the BST.
    """
    if root is not None:
        print(root.val), 
        preorder(root.left)
        preorder(root.right)