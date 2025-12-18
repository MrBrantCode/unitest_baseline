"""
QUESTION:
Write a function `find_gcd` that takes a list of integers as input and returns their greatest common divisor. The function should handle lists of any length, including empty and single-element lists. Use the `math.gcd()` function to compute the greatest common divisor of two numbers.
"""

import math

def entance(numbers):
    if len(numbers) == 0:
        return None
    elif len(numbers) == 1:
        return numbers[0]
    else:
        result = math.gcd(numbers[0], numbers[1])
        for i in range(2, len(numbers)):
            result = math.gcd(result, numbers[i])
        return result