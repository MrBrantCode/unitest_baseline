"""
QUESTION:
Write a function `factorial(n)` to calculate the factorial of a given number `n` using recursion. The function should return the product of all positive integers up to `n`. The input `n` is a non-negative integer.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)