"""
QUESTION:
Write a recursive function `fibonacci(n)` that generates the Fibonacci series up to the nth number in a functional programming style, without using loops or mutable variables.
"""

def fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib = fibonacci(n - 1)
        return fib + [fib[-1] + fib[-2]]