"""
QUESTION:
Create a function named "factorial" that takes an integer "n" as input and returns its factorial using recursion. The function should be defined in a separate module. The input "n" should be a non-negative integer. The function should return the correct factorial for any given "n" value.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)