"""
QUESTION:
Write a function called `fib` that takes an integer `n` as input and returns the nth Fibonacci number. The function should use recursion and follow these rules: if `n` is 0, return 0; if `n` is 1, return 1; otherwise, return the sum of the function called on `n-1` and `n-2`.
"""

def fib(n): 
    # Base case
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    # Recursive case
    else: 
        return fib(n-1) + fib(n-2)