"""
QUESTION:
Implement a function `calculate_result` that takes three integers `x`, `y`, and `z` as input, and returns the result after performing the following operations in sequence: 
- add `x` and `y`, 
- subtract `z` from the result, 
- multiply the result by `x`, 
- divide the result by `y`, 
- add `y` to the result, 
- subtract `z` from the result, 
- raise the result to the power of `x`, 
- calculate the square root of the result, 
- and finally round the result to the nearest integer.
"""

import math

def calculate_result(x, y, z):
    """
    This function performs a series of mathematical operations and returns the final result.

    Args:
        x (int): The first integer.
        y (int): The second integer.
        z (int): The third integer.

    Returns:
        int: The final result after performing the sequence of operations.
    """
    # add x and y
    result = x + y
    # subtract z from the result
    result -= z
    # multiply the result by x
    result *= x
    # divide the result by y
    result /= y
    # add y to the result
    result += y
    # subtract z from the result
    result -= z
    # raise the result to the power of x
    result **= x
    # calculate the square root of the result
    result = math.sqrt(result)
    # round the result to the nearest integer
    result = round(result)
    return result