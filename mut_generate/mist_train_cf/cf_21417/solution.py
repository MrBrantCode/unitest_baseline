"""
QUESTION:
Write a function named `factorial` that takes an integer `n` as input and returns its factorial, with the following restrictions: `n` should be a positive integer less than or equal to 10, and the function should use recursion without any loops or global variables.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n > 10:
        return "Input number should be less than or equal to 10."
    else:
        return n * factorial(n-1)