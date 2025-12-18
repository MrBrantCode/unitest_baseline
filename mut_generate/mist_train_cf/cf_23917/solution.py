"""
QUESTION:
Create a function `insertRec` to implement the insert operation in a Binary Search Tree. The function should take two parameters: the root node of the tree and the key to be inserted. The function should return the root of the tree after insertion. The tree node should contain an integer key and pointers to its left and right children. If the key already exists in the tree, it should not be inserted again. The function should handle the case where the tree is empty.
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insertRec(root, key):
    """
    Inserts a new key into the Binary Search Tree.
    
    Args:
    root (Node): The root node of the tree.
    key (int): The key to be inserted.
    
    Returns:
    Node: The root of the tree after insertion.
    """
    # When the tree is empty, return a new node
    if root is None:
        return Node(key)
    
    # Otherwise, recur down the tree
    if key < root.key:
        root.left = insertRec(root.left, key)
    elif key > root.key:
        root.right = insertRec(root.right, key)
    
    # Return the root
    return root