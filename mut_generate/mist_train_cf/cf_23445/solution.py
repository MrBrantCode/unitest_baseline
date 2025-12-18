"""
QUESTION:
Write a function `is_valid_bst` that determines if a given array represents a valid Binary Search Tree (BST). A valid BST is defined as a tree where the left subtree of a node contains only values less than the node's value and the right subtree contains only values greater than the node's value. The function should return True if the array is a valid BST and False otherwise.
"""

def is_valid_bst(arr):
    if len(arr) == 0:
        return True
    if len(arr) == 1:
        return True

    root_val = arr[0]
    left_subtree = [i for i in arr[1:] if i < root_val]
    right_subtree = [i for i in arr[1:] if i > root_val]

    if sorted(left_subtree) == left_subtree and sorted(right_subtree, reverse=True) == right_subtree:
        return (is_valid_bst(left_subtree) and is_valid_bst(right_subtree))
    else:
        return False