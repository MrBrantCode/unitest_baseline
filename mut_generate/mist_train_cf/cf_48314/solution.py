"""
QUESTION:
Write a function called `fib(n)` that calculates the nth Fibonacci number, where n is a positive integer. The function should return the nth Fibonacci number if n is a positive integer, and an error message otherwise.
"""

def fib(n):
    if n <= 0:
        return "Input must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(n-2):
            a, b = b, a+b
        return b