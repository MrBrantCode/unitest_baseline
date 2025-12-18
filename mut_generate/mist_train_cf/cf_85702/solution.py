"""
QUESTION:
Develop a function `factorial(n)` to compute the factorial of a provided non-negative integer `n` using recursion. The function should return the factorial of `n`, which is the product of all positive integers less than or equal to `n`.
"""

def factorial(n):
    # base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)