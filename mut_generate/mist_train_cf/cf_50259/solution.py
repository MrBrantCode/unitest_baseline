"""
QUESTION:
Implement a function called "apply_expression_tree" to utilize expression trees in a real-world scenario, such as compiling, interpreting and executing code at runtime, or performing symbolic calculations. The function should take as input an expression in the form of a tree-like data structure and return the result of the expression. The function should be flexible enough to accommodate different types of expressions and operations.
"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def apply_expression_tree(root):
    """
    Applies the expression tree and returns the result.

    Args:
    root (Node): The root of the expression tree.

    Returns:
    int: The result of the expression.
    """
    if root is None:
        return 0

    if root.value == '+':
        return apply_expression_tree(root.left) + apply_expression_tree(root.right)
    elif root.value == '-':
        return apply_expression_tree(root.left) - apply_expression_tree(root.right)
    elif root.value == '*':
        return apply_expression_tree(root.left) * apply_expression_tree(root.right)
    elif root.value == '/':
        return apply_expression_tree(root.left) / apply_expression_tree(root.right)
    else:
        return int(root.value)