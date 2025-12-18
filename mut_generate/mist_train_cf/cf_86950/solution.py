"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given non-negative integer `n` using recursion. The function should return `1` for `n = 0` or `n = 1`, and `n * factorial(n-1)` otherwise.
"""

def factorial(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    else:  # Recursive case: factorial of n is n * factorial(n-1)
        return n * factorial(n-1)