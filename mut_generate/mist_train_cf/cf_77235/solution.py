"""
QUESTION:
Create a binary expression tree for a given arithmetic equation and design a recursive function `calculate_tree` to calculate and return the final result of the expression represented by the binary tree. The function should be able to handle and properly prioritize the four main arithmetic operations: addition, subtraction, multiplication, and division. The binary tree is represented as a list of three elements where the first element represents the operation, the second element represents the left child, and the third element represents the right child. Leaf nodes are the operands, and internal nodes are operators.
"""

def calculate_tree(tree):
    if isinstance(tree, list):
        operation = tree[0]
        left = calculate_tree(tree[1])
        right = calculate_tree(tree[2])
        
        if operation == "+": return left + right
        elif operation == "-": return left - right
        elif operation == "*": return left * right
        elif operation == "/": return left / right
        else: assert False, "Unknown operation: " + operation
    else:
        return tree