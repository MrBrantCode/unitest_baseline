"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a given non-negative integer `n`. The function should use recursion, and it should handle the base case where `n` is 0 or 1. The input `n` is a non-negative integer, and the function should return the factorial of `n`.
"""

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: factorial of n is n multiplied by factorial of (n-1)
    else:
        return n * factorial(n - 1)