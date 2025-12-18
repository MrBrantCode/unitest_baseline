"""
QUESTION:
Write a recursive function called `factorial(n)` to calculate the factorial of a given number `n`. The function should only take an integer `n` as input and return the factorial of `n`. Assume that the input `n` is a non-negative integer.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)