"""
QUESTION:
Create a function `insert` to insert a new node into a binary search tree and a function `inorder` to perform an in-order traversal of the binary search tree. The binary search tree node should have a value, a left child, and a right child. The `insert` function should maintain the properties of a binary search tree where the value of each node is greater than or equal to its left child and less than or equal to its right child. The `inorder` function should print the values of the nodes in ascending order.

The `insert` function should take the root of the tree and the new value as parameters, and return the updated root. The `inorder` function should take the root of the tree as a parameter.
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert_into_bst(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert_into_bst(root.right, key)
        else:
            root.left = insert_into_bst(root.left, key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val),
        inorder_traversal(root.right)