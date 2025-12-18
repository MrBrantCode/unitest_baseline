"""
QUESTION:
Write a function named 'factorial' that calculates the factorial of a given non-negative integer without using any loops. The function should use recursion and return 1 when the input integer is 0.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)