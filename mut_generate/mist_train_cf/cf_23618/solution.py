"""
QUESTION:
Create a function to evaluate a given string as a Python expression and return the result. The function should take a string argument representing the Python expression to be evaluated.
"""

def evaluate_expression(expr):
    """
    Evaluate a given string as a Python expression and return the result.

    Args:
        expr (str): A string representing the Python expression to be evaluated.

    Returns:
        The result of the evaluated expression.
    """
    return eval(expr)