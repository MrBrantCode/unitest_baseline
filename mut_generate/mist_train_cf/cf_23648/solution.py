"""
QUESTION:
Write a function `fibonacci` that calculates the Fibonacci number at a given position `n`. The function should take an integer `n` as input and return the corresponding Fibonacci number.
"""

def fibonacci(n):
    a, b = 0, 1
    if n == 0:
        return a
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b