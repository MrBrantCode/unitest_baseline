"""
QUESTION:
Write a function called `factorial` that calculates the factorial of a given integer `n` using tail recursion optimization. The function should take an optional second argument `result` with a default value of 1. The function should return the factorial of `n` as an integer.
"""

def factorial(n, result=1):
    if n == 0:
        return result
    else:
        return factorial(n-1, result*n)