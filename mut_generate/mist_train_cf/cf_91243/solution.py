"""
QUESTION:
Implement a function named `fibonacci(n)` that calculates the nth Fibonacci number using an iterative approach with constant space complexity. The function should return the nth Fibonacci number for a given non-negative integer `n`. The Fibonacci sequence is defined as: F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1. The function should handle cases where n is 0, 1, or 2, and return the correct Fibonacci number for these base cases.
"""

def fibonacci(n):
    if n <= 0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    fib1, fib2 = 0, 1
    for _ in range(3, n+1):
        fib = fib1 + fib2
        fib1, fib2 = fib2, fib
    
    return fib2