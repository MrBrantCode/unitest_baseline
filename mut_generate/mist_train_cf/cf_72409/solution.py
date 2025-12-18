"""
QUESTION:
Write a function named "factorial" that takes one argument `n` and returns the factorial of `n`, defined as the product of all positive integers up to `n`. The function should use recursion to calculate the factorial.
"""

def entrance(n):
    if n == 0:
        return 1
    else:
        return n * entrance(n-1)