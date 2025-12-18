"""
QUESTION:
Write a function named `fibonacci_sum` that takes an integer `n` as input and returns the sum of the first `n` Fibonacci numbers.
"""

def fibonacci_sum(n):
    fib_sum = 0
    fib_prev = 0
    fib_curr = 1
    for i in range(n):
        fib_sum += fib_curr
        fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
    return fib_sum