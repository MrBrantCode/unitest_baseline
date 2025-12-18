"""
QUESTION:
Write a function called `factorial` that calculates the factorial of a given natural number x and returns the result. The function should take one integer parameter x and return its factorial as an integer. The input number x will be a non-negative integer.
"""

def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result