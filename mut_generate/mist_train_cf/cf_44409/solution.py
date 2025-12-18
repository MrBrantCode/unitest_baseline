"""
QUESTION:
Implement a function named `fibonacci` that uses recursive strategies to calculate the nth Fibonacci number. The function should use memoization to avoid duplicate computations and should not rely on any inbuilt functions or loops. The function should return the calculated Fibonacci number.
"""

def fibonacci(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fibonacci(n-1, computed) + fibonacci(n-2, computed)
    return computed[n]