"""
QUESTION:
Implement a function called `fibonacci` that takes an integer `n` as input and returns the `n`th number in the Fibonacci sequence, handling both positive and negative values of `n`. The function should be able to handle large values of `n` efficiently.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == -1:
        return 1
    else:
        a, b = 0, 1
        if n < 0:
            for _ in range(1, abs(n)):
                a, b = b - a, a
            return a
        else:
            for _ in range(n - 1):
                a, b = b, a + b
            return b