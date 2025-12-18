"""
QUESTION:
Write a function named `factorial(x)` that takes an integer `x` as input and returns its factorial, computed using an iterative solution with a loop. Do not use recursion or built-in mathematical functions.
"""

def entance(x):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result