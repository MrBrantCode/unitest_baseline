"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given positive integer `n`. The function should return the factorial of `n`. The input `n` is a positive integer.
"""

def factorial(n):
    if n > 1:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact
    else:
        return 1