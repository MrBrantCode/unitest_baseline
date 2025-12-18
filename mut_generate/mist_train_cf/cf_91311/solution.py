"""
QUESTION:
Create a function named `fibonacci(n)` that takes a large positive integer `n` (up to 10^6) as input and returns the `n`-th Fibonacci number modulo 10^9 + 7. The function should efficiently handle large inputs without overflowing.
"""

def fibonacci(n):
    # Create a list to store the Fibonacci numbers
    fib = [0, 1]
    
    # Compute the Fibonacci sequence up to n modulo 10^9 + 7
    for i in range(2, n+1):
        fib.append((fib[i-1] + fib[i-2]) % 1000000007)
    
    return fib[n]