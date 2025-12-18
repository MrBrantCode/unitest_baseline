"""
QUESTION:
Create a function named `mul_fib_y` that takes two non-negative integers `n` and `y` as input. The function should calculate the Fibonacci number at position `n` (with the sequence starting from 0) and return the result of multiplying this Fibonacci number by `y`. The function should be able to handle large values of `n` without hitting recursion limits.
"""

def mul_fib_y(n, y):
    if n == 0:
        return 0
    elif n == 1:
        return y
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b * y