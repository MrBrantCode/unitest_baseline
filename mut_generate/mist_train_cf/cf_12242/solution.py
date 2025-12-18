"""
QUESTION:
Implement a sorting function `sort_tree` that takes an array of integers as input and returns the root of a binary search tree, where the tree is built in a way that allows for efficient insertion and retrieval of elements and is sorted in ascending order. You must implement the sorting algorithm yourself without using built-in sort functions.
"""

# Node class for the tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to insert a new node into the tree
def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

# Sorting function using the binary search tree
def sort_tree(arr):
    if len(arr) == 0:
        return None

    root = Node(arr[0])
    for i in range(1, len(arr)):
        root = insert(root, arr[i])

    return root