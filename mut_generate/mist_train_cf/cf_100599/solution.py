"""
QUESTION:
Design a function `non_negative_sum(a: int, b: int) -> int` that takes two integers as input, computes their sum, and returns the sum if it's non-negative. If the sum is negative, the function should return 0. The function should also handle potential overflow errors and return 0 in such cases. The integer range limit should be considered.
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