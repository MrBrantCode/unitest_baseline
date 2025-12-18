"""
QUESTION:
Convert a given binary tree to a doubly linked list in-place, without using any extra data structures, in a depth-first manner, and with a time complexity of O(n log n). The doubly linked list should be sorted in ascending order based on the values of the nodes, with the left pointer of each node pointing to the previous node and the right pointer of each node pointing to the next node. Define a function `convert(tree)` that takes a binary tree as input and returns the head of the doubly linked list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    
    if left.data < right.data:
        left.right = merge(left.right, right)
        left.right.left = left
        left.left = None
        return left
    else:
        right.right = merge(left, right.right)
        right.right.left = right
        right.left = None
        return right

def entrance(tree):
    if not tree or not tree.left and not tree.right:
        return tree
    
    left = entrance(tree.left)
    right = entrance(tree.right)
    
    tree.left = None
    tree.right = None
    
    return merge(merge(left, tree), right)