"""
QUESTION:
Implement a function `fibonacci_iterative` that takes an integer `n` as input and returns the nth number in the Fibonacci sequence using an iterative approach. The function should handle large values of `n` efficiently.
"""

def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b