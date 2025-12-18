"""
QUESTION:
Write a recursive function called `fibonacci` that takes a non-negative integer `n` as input, generates the Fibonacci series up to the nth term, and returns the series. The function should not use any iterative methods or dynamic programming techniques.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n-1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series