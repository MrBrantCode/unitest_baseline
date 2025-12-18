"""
QUESTION:
Write a function named calculate_result that calculates the result of the expression a * b + a - b / a, where a and b are integers, using integer division (truncating any decimal points). The function should take two integer parameters, a and b, and return the calculated result.
"""

def calculate_result(a, b):
    """
    Calculate the result of the expression a * b + a - b / a using integer division.

    Args:
        a (int): The first integer parameter.
        b (int): The second integer parameter.

    Returns:
        int: The calculated result.
    """
    return a * b + a - b // a