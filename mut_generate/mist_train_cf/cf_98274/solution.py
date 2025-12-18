"""
QUESTION:
Design a function named `non_negative_sum` that takes two integers `a` and `b` as input and returns their sum as a non-negative integer. If the sum is negative, the function should return 0. The function should handle potential overflow or underflow errors and type errors by returning 0 in such cases.
"""

def non_negative_sum(a: int, b: int) -> int:
    """
    Computes the sum of two integers, ensuring that the result is non-negative.
    :param a: An integer.
    :param b: An integer.
    :return: The sum of the two integers, or 0 if the sum is negative.
    """
    try:
        # Compute the sum of the integers
        result = a + b
        # If the sum is less than zero, set the sum to zero
        if result < 0:
            result = 0
    except OverflowError:
        # Handle overflow errors
        result = 0
    except TypeError:
        # Handle type errors
        result = 0
    return result