"""
QUESTION:
Construct a function `construct_balanced_bst(arr)` that creates a balanced binary search tree from a given array of integers `arr` in such a way that the resulting tree is balanced. The function should return the root node of the constructed binary search tree.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_balanced_bst(arr):
    if not arr:
        return None
    
    mid = len(arr) // 2
    root = Node(arr[mid])
    
    root.left = construct_balanced_bst(arr[:mid])
    root.right = construct_balanced_bst(arr[mid+1:])
    
    return root