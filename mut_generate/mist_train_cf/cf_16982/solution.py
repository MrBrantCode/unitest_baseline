"""
QUESTION:
Compute the nth Fibonacci number modulo 10^9 + 7 using a non-recursive approach. The function should take a large positive integer n (up to 10^12) as input and return the corresponding Fibonacci number modulo 10^9 + 7.
"""

def fib(n):
    fib = [0, 1]  # Initialize the first two Fibonacci numbers
    for i in range(2, n+1):
        fib.append((fib[i-1] + fib[i-2]) % (10**9 + 7))  # Compute the next Fibonacci number modulo 10^9 + 7
    return fib[n]