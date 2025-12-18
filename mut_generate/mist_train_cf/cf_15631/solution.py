"""
QUESTION:
Write a tail recursive Python function named `factorial` to calculate the factorial of a number. The function must not use any loops or helper functions.
"""

def factorial(n, acc=1):
    if n == 0 or n == 1:
        return acc
    else:
        return factorial(n-1, acc*n)