"""
QUESTION:
Create a function named `fibonacci` that calculates the Fibonacci series up to `n` numbers efficiently. The function should take one integer argument `n` and return a list of Fibonacci numbers. The function should handle large values of `n` (e.g. `n > 1000`) without causing a stack overflow or excessive computation time.
"""

def fibonacci(n):
    fibSeries = []
    if n == 0:
        return fibSeries
    elif n == 1:
        fibSeries.append(0)
        return fibSeries
    elif n == 2:
        fibSeries.extend([0, 1])
        return fibSeries
    else:
        a, b = 0, 1
        fibSeries.extend([0, 1])
        for _ in range(2, n):
            fib = a + b
            fibSeries.append(fib)
            a, b = b, fib
        return fibSeries