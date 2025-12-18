"""
QUESTION:
Write a function called `evaluate_expression` that takes a string containing a Python expression as input and returns the result of the expression. The function should be able to handle basic arithmetic operations such as addition, subtraction, multiplication, and division. Note that this function should only be used with trusted input, as it poses a security risk if used with untrusted input.
"""

def evaluate_expression(expression):
    """
    Evaluate a string containing a Python expression and return the result.

    Args:
    expression (str): A string containing a Python expression.

    Returns:
    The result of the expression.

    Note:
    This function poses a security risk if used with untrusted input, as it can execute arbitrary Python code.
    """
    return eval(expression)