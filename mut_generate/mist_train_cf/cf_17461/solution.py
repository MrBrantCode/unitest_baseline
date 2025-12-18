"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given non-negative integer `x` using recursion. The function should return the calculated factorial.
"""

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)