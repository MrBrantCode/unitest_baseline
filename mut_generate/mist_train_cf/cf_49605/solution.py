"""
QUESTION:
Design a function named "factorial" that takes a single non-negative integer n as input and returns its factorial. The function should not use any built-in factorial or multiplication functions.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)