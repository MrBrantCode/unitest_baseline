"""
QUESTION:
Write a function named `fibonacci_sum` to find the sum of even Fibonacci numbers till a given prime number `n`. The function should take an integer `n` as input and return the sum of even Fibonacci numbers less than or equal to `n`.
"""

def fibonacci_sum(n):
    fib_sum = 0
    a, b = 0, 1
    while a <= n:
        if a % 2 == 0:
            fib_sum += a
        a, b = b, a + b
    return fib_sum