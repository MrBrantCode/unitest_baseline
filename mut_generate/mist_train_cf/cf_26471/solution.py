"""
QUESTION:
Implement a function `fibonacci(n)` that calculates the `n`th number in the Fibonacci sequence, where `n` is a non-negative integer and the sequence starts with 0 as the 0th number and 1 as the 1st number, with each subsequent number being the sum of the two preceding ones.
"""

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b