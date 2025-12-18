"""
QUESTION:
Create a recursive function named `factorial` that calculates the factorial of a given integer `n` with a time complexity of O(n). The function should return an error message if `n` is a negative number.
"""

def factorial(n):
    if n < 0:
        return "Input must be a non-negative integer."
    if n == 0:
        return 1
    return n * factorial(n - 1)