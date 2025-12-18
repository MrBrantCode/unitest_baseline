"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given non-negative integer `n` using recursion. The function should handle the base case where `n` equals 0 and return 1. Otherwise, it should call itself with `n-1` and multiply the result by `n`. The function should not use any loops and should only use recursive calls to calculate the factorial.
"""

def factorial(n):
    if n == 0:  # Base case
        return 1
    else:
        return n * factorial(n-1)   # Recursive call