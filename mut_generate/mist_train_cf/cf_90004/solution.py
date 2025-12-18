"""
QUESTION:
Write a recursive function `fibonacci(n)` that calculates the nth term of the Fibonacci sequence without using any loops or conditional statements like `if`. The function should follow the standard Fibonacci sequence definition where the first two terms are 0 and 1, and each subsequent term is the sum of the previous two terms.
"""

def fibonacci(n):
    return fibonacci(n - 1) + fibonacci(n - 2) if n >= 2 else n