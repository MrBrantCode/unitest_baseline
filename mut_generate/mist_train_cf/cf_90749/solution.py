"""
QUESTION:
Create a function named `factorial` to calculate the factorial of a given number using recursion. The function should take an integer `n` as input and return its factorial. The base case is when `n` equals 0 or 1, in which case the function should return 1. Otherwise, the function should call itself with the argument `n-1` and multiply the result by `n`.
"""

def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n-1)