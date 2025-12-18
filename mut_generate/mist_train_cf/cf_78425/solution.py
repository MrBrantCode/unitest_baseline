"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given number 'n'. The function should be able to handle non-negative integers and return the product of all positive integers from 1 up to 'n'.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)