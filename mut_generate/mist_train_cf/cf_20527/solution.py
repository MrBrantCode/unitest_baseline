"""
QUESTION:
Write a recursive function `factorial` that calculates the factorial of a given positive integer `n` without using any loops or helper functions. The function should have a time complexity of O(n).
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)