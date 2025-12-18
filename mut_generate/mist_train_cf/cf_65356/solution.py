"""
QUESTION:
Design a recursive function named `factorial(n)` in Python that calculates the factorial of a given non-negative integer `n`. The function should not perform error checking or input validation, so it is assumed that `n` is a non-negative integer.
"""

def factorial(n):
    #Base case: If n is 0, the factorial is 1.
    if n == 0:
        return 1
    else:
        #Recursive call: calculate the factorial of n-1 and multiply it with n
        return n * factorial(n-1)