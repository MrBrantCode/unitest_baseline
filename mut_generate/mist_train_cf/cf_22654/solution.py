"""
QUESTION:
Implement a recursive function `factorial(n)` that calculates the factorial of a non-negative integer `n` with a time complexity of O(n). The function should return an error message if `n` is negative.
"""

def factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)