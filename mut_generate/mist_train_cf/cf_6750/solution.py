"""
QUESTION:
Write a recursive function `factorial(n)` that calculates the factorial of a given non-negative integer `n`. The function should only take an integer `n` as input and return its factorial. The function should use recursion to solve the problem and should have a base case to stop the recursion.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)