"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a given number `n` using recursion, where `n` is a non-negative integer. The function should not use any loops or external libraries. The function should handle the base case where `n` is 0, and it should recursively call itself with decreasing values of `n` until the base case is reached.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)