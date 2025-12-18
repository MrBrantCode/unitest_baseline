"""
QUESTION:
Write a function `sum_of_bst` that takes the root of a binary search tree as input and returns the sum of the values of all nodes in the tree. The function should handle the case where the input tree is empty (i.e., the root is `None`).
"""

def sum_of_bst(root):
    if root is None:
        return 0
    
    return root.value + sum_of_bst(root.left) + sum_of_bst(root.right)