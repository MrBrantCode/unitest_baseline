"""
QUESTION:
Construct a function `array_to_bst(array)` that takes a sorted array of distinct integers as input and returns the root node of a balanced binary search tree. The function should preserve the order of elements in the array and ensure that the resulting tree is a valid binary search tree.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def array_to_bst(array):
    if not array:
        return None

    mid = len(array) // 2

    root = Node(array[mid])

    root.left = array_to_bst(array[:mid])
    root.right = array_to_bst(array[mid+1:])

    return root