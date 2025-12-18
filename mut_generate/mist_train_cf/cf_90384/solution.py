"""
QUESTION:
Write a function `fibonacci(n)` that generates the Fibonacci sequence up to the `n`th number using iterative methods. The function should be optimized to handle large numbers efficiently and avoid memory overflow errors or excessive runtime.
"""

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib