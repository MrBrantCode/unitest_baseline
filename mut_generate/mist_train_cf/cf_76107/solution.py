"""
QUESTION:
Write a function named `fibonacci(n)` that returns the `n`-th Fibonacci number, where the sequence is defined as 0 for `n=0` and 1 for `n=1`, and each subsequent number is the sum of the previous two. The function should return the calculated Fibonacci number.
"""

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a