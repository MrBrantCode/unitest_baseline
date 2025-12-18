"""
QUESTION:
Create a function `check_division_by_zero` that takes the root of a binary expression tree as input and returns True if the equation represented by the tree contains a division by zero error, and False otherwise. The binary expression tree is constructed using a Node class with a value and left and right child nodes. The function should recursively traverse the tree, checking for division operations with a zero denominator.
"""

class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def check_division_by_zero(node):
    if node is None:
        return False
    if node.value == '/':
        if node.right.value == 0:
            return True
    return check_division_by_zero(node.left) or check_division_by_zero(node.right)