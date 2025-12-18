"""
QUESTION:
Implement a function named `sort_tree` that takes an array of integers as input and returns the root of a binary search tree (BST) containing the elements of the array in ascending order. The function should not use built-in sorting algorithms and should ensure that the BST is constructed in a way that allows for efficient insertion and retrieval of elements.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def sort_tree(arr):
    if len(arr) == 0:
        return None

    root = Node(arr[0])
    for i in range(1, len(arr)):
        root = insert(root, arr[i])

    return root