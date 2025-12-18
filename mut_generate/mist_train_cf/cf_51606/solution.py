"""
QUESTION:
Write a recursive function `factorial(n)` that calculates the factorial of a given non-negative integer `n` using recursion. Assume that the input `n` is a non-negative integer. Implement the function to handle the base case where `n` equals 0 and recursively call itself until the base case is met.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)