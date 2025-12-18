"""
QUESTION:
Write a function named `Fibonacci` that takes a non-negative integer `n` as input and returns the nth Fibonacci number. Implement this function with optimal computational and storage complexities, considering that only the nth Fibonacci number is needed, not the entire sequence.
"""

def Fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a