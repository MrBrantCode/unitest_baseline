"""
QUESTION:
Write an efficient function `fibonacci(n)` to generate the Fibonacci sequence up to the `n`th number using an iterative method, ensuring it can handle large numbers without causing memory overflow errors or excessive runtime.
"""

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib