"""
QUESTION:
Write a function `fibonacci(n)` to calculate the n-th number of the Fibonacci sequence using recursion, where F(n) = F(n-1) + F(n-2) with initial conditions F(0) = 0 and F(1) = 1. The function should take an integer `n` as input and return the corresponding Fibonacci number.
"""

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)