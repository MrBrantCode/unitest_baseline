"""
QUESTION:
Implement a recursive function named `factorial` that calculates the factorial of a given positive integer `n` with a time complexity of O(n). The function should not use any loops or iteration.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)