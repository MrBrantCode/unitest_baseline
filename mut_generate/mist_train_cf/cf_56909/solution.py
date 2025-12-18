"""
QUESTION:
Implement a function named `evaluate` that takes the root of a binary expression tree as input, where each node represents an operator (+, -, *, /) or an operand (an integer). The function should evaluate the arithmetic expression represented by the tree, handling the rules of precedence and association, and return the result as an integer. The input tree is assumed to be valid, and the function should handle division by non-zero integers.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def evaluate(root):
    if root.val.isdigit():
        return int(root.val)
    else:
        if root.val == '+':
            return evaluate(root.left) + evaluate(root.right)
        elif root.val == '-':
            return evaluate(root.left) - evaluate(root.right)
        elif root.val == '*':
            return evaluate(root.left) * evaluate(root.right)
        elif root.val == '/':
            return int(evaluate(root.left) / evaluate(root.right))