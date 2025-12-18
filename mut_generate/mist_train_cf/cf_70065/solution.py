"""
QUESTION:
Given a simple arithmetic expression tree where leaf nodes represent operands (numbers) and non-leaf nodes represent operators (+ or *), write a function `evaluate(node)` to calculate and return the resultant value of the expression. The function should recursively traverse the tree, performing the operations at each node until it reaches the leaf nodes. Assume that the expression tree is valid and doesn't require error checking or validation.
"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def evaluate(node):
    if node.value == '+':
        return evaluate(node.left) + evaluate(node.right)
    elif node.value == '*':
        return evaluate(node.left) * evaluate(node.right)
    else:
        return int(node.value)