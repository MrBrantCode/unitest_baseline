"""
QUESTION:
Write a Python function named `factorial` that calculates the factorial of a given integer `n` using recursion. The function should not use iteration.
"""

def factorial(n):
    # Base case: 0! = 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)