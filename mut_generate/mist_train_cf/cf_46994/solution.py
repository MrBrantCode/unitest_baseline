"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of an integer `n`. If `n` is negative, return a message indicating that the factorial of a negative number is undefined.
"""

def entance(n):
    if n < 0:
        return "Undefined. Factorial of a negative number doesn't exist."
    elif n == 0 or n == 1:
        return 1
    else:
        return n*entance(n-1)