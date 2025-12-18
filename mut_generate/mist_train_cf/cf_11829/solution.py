"""
QUESTION:
Write a function `evaluate_expression` to evaluate the given mathematical expression "(3 * 5 + 4) / 2 + 10 - 3 * 2" following the order of operations (PEMDAS) and return the result as a float.
"""

def evaluate_expression(expression):
    """
    Evaluate the given mathematical expression following the order of operations (PEMDAS) and return the result as a float.

    Args:
        expression (str): The mathematical expression to be evaluated.

    Returns:
        float: The result of the expression evaluation.
    """
    return eval(expression)