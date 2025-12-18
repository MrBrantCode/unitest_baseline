"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given non-negative integer `x` using recursion and returns the result. The function should handle the base case where `x` is 0.
"""

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)