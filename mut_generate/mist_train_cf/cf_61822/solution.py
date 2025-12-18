"""
QUESTION:
Implement a function `factorial(n)` that calculates the factorial of a given number `n` using tail recursion optimization.
"""

def factorial(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial(n-1, n * acc)