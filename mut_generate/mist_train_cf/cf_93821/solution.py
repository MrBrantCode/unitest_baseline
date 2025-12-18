"""
QUESTION:
Write a recursive Python function named `factorial` to calculate the factorial of a given number. The function must be tail recursive and should not use any loops or helper functions. It should take an integer `n` as input and return its factorial. If desired, the function can take an additional argument `acc` to accumulate the result, with a default value of 1.
"""

def factorial(n, acc=1):
    if n == 0 or n == 1:
        return acc
    else:
        return factorial(n-1, acc*n)