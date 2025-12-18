"""
QUESTION:
Write a function named `deleteNode` that deletes a given node with a specified key from a balanced binary search tree (BST) and returns the root node of the updated BST. The function should take two parameters: the root node of the BST and the key of the node to be deleted. The time complexity for the deletion operation should be O(log n).
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

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
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.key = minValueNode(root.right).key
        root.right = deleteNode(root.right, root.key)
    return root