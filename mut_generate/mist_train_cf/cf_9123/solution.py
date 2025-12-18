"""
QUESTION:
Write a function named `factorial(n)` that calculates the factorial of a given integer `n` using recursion, where `n! = n * (n-1)!`. The function should handle the base case when `n` equals 0 or 1, returning 1 in these cases.
"""

def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n-1)