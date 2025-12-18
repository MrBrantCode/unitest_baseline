"""
QUESTION:
Create a function named `fibonacci` that calculates the nth Fibonacci number using a recursive approach. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. The function should take an integer `n` as input and return the corresponding Fibonacci number.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)