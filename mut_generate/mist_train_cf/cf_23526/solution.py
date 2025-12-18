"""
QUESTION:
Write a function `factorial` that calculates the product of all positive integers up to a given number `n`. The function should take one argument `n` and return the product of all integers from 2 to `n` (inclusive). Implement the function in a way that minimizes time complexity.
"""

def factorial(n):
    if n < 2:
        return 1
    product = 2
    for i in range(3, n + 1):
        product *= i
    return product