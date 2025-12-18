"""
QUESTION:
Create a function named `fibonacci` that takes a positive integer `n` (up to 10^6) as input and returns the `n`-th Fibonacci number modulo 10^9 + 7. The function should be efficient for large inputs.
"""

def fibonacci(n):
    fib = [0, 1]
    
    for i in range(2, n+1):
        fib.append((fib[i-1] + fib[i-2]) % 1000000007)
    
    return fib[n]