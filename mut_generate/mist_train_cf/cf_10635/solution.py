"""
QUESTION:
Create a function called `fib` that takes a positive integer `n` as input and returns the `n`th element of the Fibonacci sequence. The function should handle invalid inputs where `n` is less than or equal to 0.
"""

def fib(n):
    if n <= 0:
        return "N should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)