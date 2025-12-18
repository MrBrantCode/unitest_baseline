"""
QUESTION:
Write a function called `fibonacci(n)` that generates the Fibonacci sequence up to the nth term and returns the count of numbers in the sequence that are greater than half-a-million (500000), where 1 <= n <= 50.
"""

def fibonacci(n):
    fib = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return sum(i > 500000 for i in fib)