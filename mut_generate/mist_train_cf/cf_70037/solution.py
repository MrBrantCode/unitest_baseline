"""
QUESTION:
Write a recursive function `factorial(n)` that calculates the factorial of a non-negative integer `n`. The function should use recursion to compute the result and include a base case to stop the recursion.
"""

def entance(n):
    # base case: factorial of 0 is 1
    if n == 0:
        return 1
    # recursive case: n! = n * (n-1)!
    else:
        return n * entance(n-1)