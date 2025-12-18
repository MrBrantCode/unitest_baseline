"""
QUESTION:
Construct a function named `binarySearchTree` that takes a sorted list of integers as input and returns the root node of a balanced binary search tree. The tree should be balanced such that the height difference between the left and right subtree is at most 1. The function should handle empty input lists and recursively construct the binary search tree.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def binarySearchTree(items):
    if not items:
        return None
    
    mid = len(items) // 2
    rootValue = items[mid]
    
    root = Node(rootValue)
    root.left = binarySearchTree(items[:mid])
    root.right = binarySearchTree(items[mid + 1:])
    
    return root