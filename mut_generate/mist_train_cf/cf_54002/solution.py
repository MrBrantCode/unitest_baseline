"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given non-negative integer using a recursive algorithm. The function should take one argument `n` and return the factorial of `n`. The function should follow the mathematical definition of factorial: `n! = n * (n-1)!`, where `0!` is defined to be `1`.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)