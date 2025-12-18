"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a given integer `x` using recursion. The function should return the calculated factorial value. The input `x` is a non-negative integer.
"""

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)