"""
QUESTION:
Convert a binary tree to a doubly linked list in-place, without using any extra data structures. The conversion should be done in a depth-first manner and the doubly linked list should be sorted in ascending order based on the values of the nodes. The left pointer of each node should point to the previous node in the doubly linked list and the right pointer of each node should point to the next node in the doubly linked list. The time complexity of the algorithm should be O(n log n), where n is the number of nodes in the binary tree. Implement a function `convert(tree)` that takes a binary tree as input and returns the head of the doubly linked list.
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
        right.left = None
        right.right = merge(left, right.right)
        right.right.left = right
        return right

def tree_to_doubly_linked_list(tree):
    if not tree or not tree.left and not tree.right:
        return tree
    
    left = tree_to_doubly_linked_list(tree.left)
    right = tree_to_doubly_linked_list(tree.right)
    
    tree.left = None
    tree.right = None
    
    return merge(merge(left, tree), right)