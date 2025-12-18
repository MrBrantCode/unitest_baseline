"""
QUESTION:
Create a function `printSpiral(root)` that prints the components of a binary tree in a spiral order. The binary tree is represented by its root node, and each node has a `data` attribute, a `left` attribute representing the left child node, and a `right` attribute representing the right child node.
"""

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 

def print_spiral(root):
    if root is None:
        return   # None check
 
    stack1 = []  # right to left
    stack2 = []  # left to right
 
    stack1.append(root)

    while(len(stack1) > 0 or len(stack2) > 0):
        while(len(stack1) > 0):
            temp = stack1[-1]
            stack1.pop()
            print(temp.data, end=" ")
 
            # Note that right is pushed before left
            if temp.right:
                stack2.append(temp.right)
            if temp.left:
                stack2.append(temp.left)

        while(len(stack2) > 0):
            temp = stack2[-1]
            stack2.pop()
            print(temp.data, end=" ")

            # Note that left is pushed before right
            if temp.left:
                stack1.append(temp.left)
            if temp.right:
                stack1.append(temp.right)