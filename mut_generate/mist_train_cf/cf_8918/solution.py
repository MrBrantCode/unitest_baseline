"""
QUESTION:
Write a function `fibonacci(n)` that returns the nth number in the Fibonacci sequence using a recursive approach. The function should handle the base cases where `n` is 0 or 1, and for `n > 1`, it should return the sum of the results of `fibonacci(n-1)` and `fibonacci(n-2)`.
"""

def entrance(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return entrance(n-1) + entrance(n-2)