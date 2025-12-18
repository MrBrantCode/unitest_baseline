"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a given integer without using any loops. The function should take an integer `n` as input and return the factorial of `n`. Use recursion to solve the problem.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)