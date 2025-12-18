"""
QUESTION:
Design a function `composite_gcd` that takes two parameters, `start` and `end`, representing the start and end of a range (inclusive). The function should return the greatest common divisor of all composite numbers within the specified range. The inputs `start` and `end` are guaranteed to be positive integers, and `start` is less than or equal to `end`.
"""

import math

def composite_gcd(start, end):
    """
    This function calculates the greatest common divisor of all composite numbers within a specified range.

    Parameters:
    start (int): The start of the range (inclusive)
    end (int): The end of the range (inclusive)

    Returns:
    int: The greatest common divisor of all composite numbers in the range
    """

    # Function to check if a number is composite
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return True
        return False

    # Function to calculate the greatest common divisor of two numbers using the Euclidean algorithm
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    # Initialize the greatest common divisor with the first composite number in the range
    composite_gcd_result = next((i for i in range(start, end + 1) if is_composite(i)), None)

    # If no composite numbers are found in the range, return 1
    if composite_gcd_result is None:
        return 1

    # Calculate the greatest common divisor of all composite numbers in the range
    for i in range(start, end + 1):
        if is_composite(i):
            composite_gcd_result = gcd(composite_gcd_result, i)

    return composite_gcd_result