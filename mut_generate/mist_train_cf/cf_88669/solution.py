"""
QUESTION:
Create a function called `factorial(n)` that calculates the factorial of a given number `n`. The function should take one argument `n`, which is the input number. The function should check if the input is a positive integer and return an error message if it is not. It should have a time complexity of O(n) and be able to handle large numbers without causing overflow or memory issues. The function should also include error handling for negative numbers and floating-point numbers, and return appropriate error messages for these cases.
"""

import sys

def factorial(n):
    # Error handling for non-positive integers
    if not isinstance(n, int) or n <= 0:
        return "Error: Input must be a positive integer"
    
    # Base case
    if n == 1:
        return 1
    
    # Recursive case
    if n > sys.getrecursionlimit() / 2:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    else:
        return n * factorial(n - 1)