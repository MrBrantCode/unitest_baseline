"""
QUESTION:
Create a function called `calculate_result` that takes two large integers `a` and `b` as input, where `a` and `b` can be up to 10^18 and can be negative. The function should return the sum of `a` and `b` as a floating-point number rounded to two decimal places.
"""

def calculate_result(a, b):
    """
    This function calculates the sum of two large integers a and b and returns the result as a floating-point number rounded to two decimal places.

    Args:
        a (int): The first large integer.
        b (int): The second large integer.

    Returns:
        float: The sum of a and b rounded to two decimal places.
    """
    return round(float(a + b), 2)