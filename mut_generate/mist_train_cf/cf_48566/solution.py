"""
QUESTION:
Write a function `canRepresentBST(preOrder)` to check if a given array can represent a preorder traversal of a binary search tree. The function should take a list of integers `preOrder` as input and return `True` if the array can represent a preorder traversal of a binary search tree, and `False` otherwise.
"""

def canRepresentBST(preOrder): 
    stack = []
    root = float("-inf") 

    for value in preOrder: 
        if value < root: 
            return False
        while(len(stack) > 0 and stack[-1] < value) : 
            root = stack.pop() 
        stack.append(value) 

    return True