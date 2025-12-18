"""
QUESTION:
Create a function named `balanced_bst(arr)` that takes a sorted array of integers as input and returns the root node of a balanced binary search tree constructed from the array. The function should ensure that the tree is balanced by selecting the middle element of the array as the root and recursively constructing the left and right subtrees. The function should return `None` if the input array is empty.
"""

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def balanced_bst(arr):
    if not arr:
        return None

    mid = (len(arr)) // 2

    root = Node(arr[mid])

    root.left = balanced_bst(arr[:mid])

    root.right = balanced_bst(arr[mid+1:])
    return root