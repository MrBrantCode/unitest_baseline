"""
QUESTION:
Create a function named `fact` that calculates the factorial of a given non-negative integer `n`. The function should return the product of all positive integers up to `n`. If `n` equals 0, the function should return 1.
"""

def fact(n: int):
    """Returns the factorial of n."""
    if n == 0:
        return 1
    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res