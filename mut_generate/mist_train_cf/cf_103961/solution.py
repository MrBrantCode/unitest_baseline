"""
QUESTION:
Write a function `fibonacci(n)` that returns the nth Fibonacci number. Assume that `n` will always be a positive integer. Use an iterative approach to solve this problem.
"""

def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib1 = 0
        fib2 = 1
        for i in range(3, n+1):
            fib = fib1 + fib2
            fib1 = fib2
            fib2 = fib
        return fib2