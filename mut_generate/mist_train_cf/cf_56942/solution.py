"""
QUESTION:
Write a function named `fib` that calculates the nth Fibonacci number using a recursive algorithm. The function should take an integer `n` as input and return the corresponding Fibonacci number. The function should handle cases where `n` is 0, 1, or 2, and recursively call itself to calculate the Fibonacci number for larger values of `n`. The input `n` should be a positive integer.
"""

def fib(n):
    if n <= 0:
        return "Input should be positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)