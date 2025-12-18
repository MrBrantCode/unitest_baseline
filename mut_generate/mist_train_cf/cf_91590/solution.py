"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given number. The function should only accept positive integers and return an error message for any other input. The function should use recursion and have a maximum recursion depth of 1000.
"""

import sys
sys.setrecursionlimit(1000)

def factorial(n):
    if not isinstance(n, int) or n < 0:
        return "Error: Input should be a positive integer."
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)