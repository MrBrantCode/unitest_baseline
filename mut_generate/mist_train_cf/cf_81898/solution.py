"""
QUESTION:
Develop a function called `fibonacci(n)` that generates and returns the first 'n' components of the Fibonacci series, where 'n' is a positive integer. The function should start the series from 0 and 1, and the returned series should be a list of integers.
"""

def fibonacci(n):
    fib_series = []
    a, b = 0, 1

    while len(fib_series) < n:
        fib_series.append(a)
        a, b = b, a + b

    return fib_series