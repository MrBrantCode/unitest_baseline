"""
QUESTION:
Implement a function named `factorial` that calculates the factorial of a given non-negative integer using tail recursion. The function should take two parameters: the input number `n` and an optional accumulator `acc` with a default value of 1. If `n` is negative, the function should return an error message.
"""

def factorial(n, acc=1):
    if n < 0:
        return "Error: Input must be a non-negative number."
    elif n == 0:
        return acc
    else:
        return factorial(n-1, n*acc)