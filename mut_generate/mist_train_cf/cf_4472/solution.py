"""
QUESTION:
Write a function `get_result(n)` that calculates the sum of all Fibonacci numbers up to the nth number, modulo 10^9 + 7, handling negative input values by returning -1. Ensure the function works correctly for large input values.
"""

def get_result(n):
    if n < 0:
        return -1
    fib = [0, 1] 
    for i in range(2, n+1): 
        fib.append((fib[i-2] + fib[i-1]) % (10**9 + 7)) 
    return sum(fib) % (10**9 + 7)