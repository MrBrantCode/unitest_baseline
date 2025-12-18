"""
QUESTION:
Implement a function called `fibonacci` that takes an integer `n` as input and returns the Fibonacci number at index `n` using a recursive approach with a time complexity of O(2^n). The function should not use any built-in mathematical functions or libraries for calculating Fibonacci numbers. The function should handle base cases where `n` is 0 or 1, and for `n` greater than 1, it should recursively call itself with `n-1` and `n-2` as arguments and return their sum.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)