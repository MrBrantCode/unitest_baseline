"""
QUESTION:
Design a function named `sort_list` that takes a list of integers as input and returns the sorted list. The function must use a binary search tree to sort the list, where each node in the tree has a key value and points to its left and right children. The function should insert the integers into the binary search tree and then perform an in-order traversal to get the sorted list.
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    result = []
    if root:
        result = inorder(root.left)
        result.append(root.val)
        result = result + inorder(root.right)
    return result

def sort_list(input_list):
    root = None
    for element in input_list:
        root = insert(root, element)
    return inorder(root)