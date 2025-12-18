"""
QUESTION:
Write a function named `fibonacci(n)` that calculates the nth term of the Fibonacci series using an iterative procedure. The function should take an integer `n` as input and return the corresponding Fibonacci number. The solution should aim for high computational efficiency and optimal algorithmic complexity.
"""

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a