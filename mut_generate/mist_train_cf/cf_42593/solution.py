"""
QUESTION:
Create a function called `evaluate_expression` that takes a string `expression` as input, representing a mathematical expression with basic arithmetic operations and parentheses, and returns the result of the evaluated expression. The expression may contain addition, subtraction, multiplication, and division, and the function should handle the order of operations correctly.
"""

def evaluate_expression(expression):
    """
    Evaluate a mathematical expression with basic arithmetic operations and parentheses.

    Args:
    expression (str): A string representing a mathematical expression.

    Returns:
    result: The result of the evaluated expression.
    """
    return eval(expression)