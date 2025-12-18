"""
QUESTION:
Implement a function called `fibonacci` that takes an integer `n` as input and returns the `n`th Fibonacci number. The Fibonacci sequence is a series of numbers where the first two numbers are 0 and 1, and each subsequent number is the sum of the previous two numbers. The function should use a recursive algorithm and should not use any iterative approach or data structures like arrays or dictionaries.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)