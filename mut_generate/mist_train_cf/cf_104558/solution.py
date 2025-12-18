"""
QUESTION:
Implement a function named `factorial` that takes a positive integer `n` as input and returns its factorial. The function must use recursion and should not take any additional parameters. The input `n` is guaranteed to be a non-negative integer, but it may be large enough to cause a stack overflow.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)