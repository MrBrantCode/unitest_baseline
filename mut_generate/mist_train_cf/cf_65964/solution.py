"""
QUESTION:
Implement a function to evaluate an arithmetic expression represented as a self-balancing binary expression tree (AVL tree) that handles addition, subtraction, and multiplication operations. The function should take the root node of the AVL tree as input and return the result of the expression. The function should also handle cases where the node values are operators or operands.
"""

def evaluate_expression(root):
    if root is not None:
        if root.value in "+*-":
            left_value = evaluate_expression(root.left)
            right_value = evaluate_expression(root.right)
            return eval(f"{left_value}{root.value}{right_value}")
        else:
            return int(root.value)