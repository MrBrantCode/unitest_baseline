"""
QUESTION:
Write a function `factorial` that calculates the factorial of a given integer `n` using tail recursion optimization. The function should take an optional accumulator `acc` with a default value of 1. If `n` is less than 0, the function should return an error message. If `n` is 0 or a positive integer, the function should return the calculated factorial.
"""

def factorial(n, acc=1):
    if n < 0:
        return "Error: Factorial of a negative number is undefined."
    elif n == 0:
        return acc
    else:
        return factorial(n - 1, acc * n)