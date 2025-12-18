"""
QUESTION:
Write a function named factorial that calculates the factorial of a given number n. The function should return the factorial of n. The input number n is a non-negative integer.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)