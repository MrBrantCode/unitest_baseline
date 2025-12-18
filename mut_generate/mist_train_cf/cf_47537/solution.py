"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given integer `n`. The function should use recursion and handle the base case correctly. The function should return `1` when `n` is `0`.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)