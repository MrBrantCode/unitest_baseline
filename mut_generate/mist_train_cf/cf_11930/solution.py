"""
QUESTION:
Write a function named factorial(n) that calculates the factorial of a given integer n. The function should recursively calculate the factorial, where the factorial of 0 is 1, and for any other number n, it is n multiplied by the factorial of n-1.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)