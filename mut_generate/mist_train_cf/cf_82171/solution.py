"""
QUESTION:
Construct a recursive function `fibonacci(n)` that calculates the nth Fibonacci number using memoization to optimize the computation and avoid redundant calculations. The function should take an integer `n` as input and return the corresponding Fibonacci number. Implement memoization using a dictionary to store intermediate results.
"""

def fibonacci(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fibonacci(n-1, computed) + fibonacci(n-2, computed)
    return computed[n]