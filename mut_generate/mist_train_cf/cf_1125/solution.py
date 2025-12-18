"""
QUESTION:
Write a Python function named `factorial` that calculates the factorial of a given number using recursion. The function should not use any built-in functions or libraries to calculate the factorial. The input number `n` will be between 1 and the maximum limit of the system's integer size. The function should return the calculated factorial.
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)