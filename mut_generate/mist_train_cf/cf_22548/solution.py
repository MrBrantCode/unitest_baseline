"""
QUESTION:
Write a function `evaluate_expression` that takes a string of a mathematical expression as input and returns the result of the expression after applying the correct operator precedence. The input expression will only contain integers, the four basic arithmetic operators (+, -, *, /), and parentheses to group subexpressions.
"""

def evaluate_expression(expression):
    """
    Evaluate a mathematical expression with correct operator precedence.

    Args:
    expression (str): A string of a mathematical expression containing integers, 
                      basic arithmetic operators, and parentheses.

    Returns:
    int: The result of the expression after applying the correct operator precedence.
    """
    return eval(expression)