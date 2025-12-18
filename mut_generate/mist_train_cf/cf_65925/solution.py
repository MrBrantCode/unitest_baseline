"""
QUESTION:
Write a function called `factorial` that calculates the factorial of a given integer. The function should take one argument `n` and return its factorial value. The function should be able to calculate the factorial for the first 20 integers, i.e., from 0 to 20.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact