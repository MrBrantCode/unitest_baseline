"""
QUESTION:
Construct a function `construct_balanced_bst(arr)` that takes a list of integers `arr` as input and returns the root node of a balanced binary search tree constructed from the elements of `arr`. The function should ensure that the resulting tree is balanced by following the approach of sorting the input array and recursively constructing the tree by selecting the middle element as the root. The function should handle cases where the input array is empty.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_balanced_bst(arr):
    if not arr:
        return None
    
    arr.sort()
    mid = len(arr) // 2
    root = Node(arr[mid])
    
    root.left = construct_balanced_bst(arr[:mid])
    root.right = construct_balanced_bst(arr[mid+1:])
    
    return root