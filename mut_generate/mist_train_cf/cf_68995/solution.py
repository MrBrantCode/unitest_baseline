"""
QUESTION:
Create a Python function named `factorial` that calculates the factorial of a given integer `n` using recursion. The function should handle the base case where `n` is 0 or 1, and the recursive case where `n` is greater than 1. The function should only take one integer argument `n` and return its factorial.
"""

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)