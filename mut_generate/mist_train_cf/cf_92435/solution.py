"""
QUESTION:
Implement a function named factorial that calculates the factorial of a positive integer using recursion, with a time complexity of O(n). The function should not use any loops or iteration. The function should take one argument, a positive integer n, and return the factorial of n.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)