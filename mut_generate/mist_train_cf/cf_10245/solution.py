"""
QUESTION:
Write a function named factorial that calculates the factorial of a given integer using a recursive algorithm, without any loops or iterative constructs. The function should take an integer n as input and return the factorial of n.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)