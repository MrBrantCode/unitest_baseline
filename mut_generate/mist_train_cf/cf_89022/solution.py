"""
QUESTION:
Implement a function named `factorial` that calculates the factorial of a given non-negative integer using tail recursion. The function should take two parameters: `n` and `acc`, where `n` is the number for which to calculate the factorial, and `acc` is the accumulator with a default value of 1. If `n` is a negative number, the function should return an error message.
"""

def factorial(n, acc=1):
    if n < 0:
        return "Error: Input must be a non-negative number."
    elif n == 0:
        return acc
    else:
        return factorial(n-1, n*acc)