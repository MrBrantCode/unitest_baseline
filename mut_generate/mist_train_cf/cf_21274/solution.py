"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given number `n` using recursion. The function should take an integer `n` as input and return the factorial of `n`. The function should use recursion to break down the problem into smaller subproblems until a base case is reached.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)