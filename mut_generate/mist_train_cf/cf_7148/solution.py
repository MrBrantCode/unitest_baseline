"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given positive integer `n`. The function should return an error message if `n` is not a positive integer or is greater than 100. The function should be able to handle large numbers efficiently and without any loss of precision.
"""

import math

def factorial(n):
    if n < 0 or n > 100:
        return "Invalid input. Please enter a positive number less than or equal to 100."
    else:
        return math.factorial(n)