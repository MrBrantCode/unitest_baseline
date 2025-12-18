"""
QUESTION:
Create a function named `list_intersection` that takes two lists `l1` and `l2` as input and returns their intersection in a sorted, deduplicated list. The function should not use any inherent list functions for finding the intersection, but instead, build a binary search tree from the elements of the first list. It should handle edge cases where one or both input lists are empty.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if root.value < value:
            root.right = insert(root.right, value)
        else:
            root.left = insert(root.left, value)
    return root

def search(root, value):
    if root is None or root.value == value:
        return root
    if root.value < value:
        return search(root.right,value)
    return search(root.left,value)

def list_intersection(l1: list, l2: list):
    #Edge case of both sets being empty
    if not l1 and not l2: 
        return []
    
    #Edge case of one of the sets being empty
    elif not l1 or not l2: 
        return []

    result = []
    #Building the binary tree with elements of the first list
    root = None
    for element in l1:
        root = insert(root, element)
    #For each element in l2, if found in BST, append to result
    for element in l2:
        if search(root, element):
            result.append(element)
    #Returning the sorted, deduplicated list
    result = list(dict.fromkeys(result))
    result.sort()
    return result