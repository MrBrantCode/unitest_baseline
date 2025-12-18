"""
QUESTION:
Write a function named `factorial(n)` that calculates the factorial of a non-negative integer `n`. The function should handle edge cases where `n` is a negative number or not an integer. Optimize the function to efficiently handle large integers.
"""

def factorial(n):
    if not isinstance(n, int) or n < 0:
        return "Error: Input should be a non-negative integer."

    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)