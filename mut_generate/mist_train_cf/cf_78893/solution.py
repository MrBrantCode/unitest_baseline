"""
QUESTION:
Implement a function named `factorial` that calculates the factorial of a given non-negative integer `n`. The function should return the result of the factorial calculation. 

The function should be able to handle the base case where `n` is 0, in which the function should return 1.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)