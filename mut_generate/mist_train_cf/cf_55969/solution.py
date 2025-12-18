"""
QUESTION:
Implement a function `deleteNode(root, key)` that deletes a node with a given key from a binary search tree. The function should maintain the BST properties and consider the three cases of node deletion: leaf node, non-leaf node with one child, and non-leaf node with two children.
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

def deleteNode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None :
            temp = root.right
            root = None
            return temp
        elif root.right is None :
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right , temp.key)
    return root