"""
QUESTION:
Write a function `evaluate_expression(x, y)` that takes two integer parameters, evaluates the expression `(x = 2 && y > x)`, and returns a string containing the output of `y + 1` and `x` without any space. Note that the expression contains an assignment operator (=) instead of a comparison operator (==).
"""

def evaluate_expression(x, y):
    """
    Evaluates the expression (x = 2 && y > x) and returns a string containing 
    the output of y + 1 and x without any space.

    Args:
        x (int): The first integer parameter.
        y (int): The second integer parameter.

    Returns:
        str: A string containing the output of y + 1 and x without any space.
    """
    if y > 2:  # corrected the condition to use comparison operator (==) instead of assignment operator (=)
        x = 2
    return str(y + 1) + str(x)