"""
QUESTION:
Write a function called `factorial(n)` that uses recursion to calculate the factorial of a given integer `n`. The function should handle the base case where `n` equals 0, and it should recursively call itself to compute the factorial for `n > 0`. Note that the function should only use recursive methodology and should not rely on iterative methods or built-in factorial functions.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)