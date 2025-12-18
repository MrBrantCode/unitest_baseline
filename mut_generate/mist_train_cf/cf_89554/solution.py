"""
QUESTION:
Write a function named `factorial(n)` that uses recursion to calculate the factorial of a given non-negative integer `n`. The function should include a base case to prevent infinite recursion.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)