"""
QUESTION:
Write a function `percentage_difference` that calculates the percentage difference between the positive square roots of two perfect square numbers. The function should take two integers as input, calculate their positive square roots, find the difference in terms of percentage to the nearest whole number, and return the result. Assume that the inputs are perfect square numbers.
"""

import math

def percentage_difference(num1, num2):
    """
    Calculate the percentage difference between the positive square roots of two perfect square numbers.

    Args:
    num1 (int): The first perfect square number.
    num2 (int): The second perfect square number.

    Returns:
    int: The percentage difference between the square roots of num1 and num2 to the nearest whole number.
    """

    # Calculate the square roots of num1 and num2
    sqrt_num1 = math.sqrt(num1)
    sqrt_num2 = math.sqrt(num2)

    # Calculate the percentage difference
    if sqrt_num2 == 0:
        return 0  # or any other value that makes sense for your use case

    percentage_diff = ((sqrt_num1 - sqrt_num2) / sqrt_num2) * 100

    # Return the rounded percentage difference
    return round(percentage_diff)