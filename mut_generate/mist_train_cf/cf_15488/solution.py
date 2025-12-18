"""
QUESTION:
Write a function `fibonacci(n)` that takes a positive integer `n` as input and returns the nth number in the Fibonacci sequence. The function should handle cases where `n` is not a positive integer.
"""

def fibonacci(n):
    if n <= 0:
        return "Invalid input! Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b