"""
QUESTION:
Implement a function called `factorial` that calculates the factorial of a given positive integer `n`. The function should use recursion and include a base case to prevent infinite loops. The function should take one argument `n` and return the factorial of `n`.
"""

def factorial(n):
    #Base Case
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)