"""
QUESTION:
Implement a function named `find_size` that calculates the total number of nodes in a binary tree with parent pointers. The function should take the root node as an argument and return the total number of nodes in the tree. The time complexity of the function should be O(n), where n is the number of nodes in the tree, and the space complexity should be O(h), where h is the height of the tree. Assume that the input tree is a valid binary tree with no cycles.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

def find_size(root):
    if root is None:
        return 0
    
    size = 1
    if root.left is not None:
        size += find_size(root.left)
    if root.right is not None:
        size += find_size(root.right)
    
    return size