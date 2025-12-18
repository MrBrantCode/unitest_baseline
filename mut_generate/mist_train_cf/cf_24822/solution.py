"""
QUESTION:
Write a function `calculate_expression` that takes a string containing a mathematical expression as input and returns the result of the expression. The function should be able to handle basic arithmetic operations (+, -, *, /).
"""

def calculate_expression(expression):
    """
    This function evaluates a string containing a mathematical expression.
    
    Parameters:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    result: The result of the mathematical expression.
    """
    return eval(expression)