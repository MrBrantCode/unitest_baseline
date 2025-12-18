"""
QUESTION:
Implement a function `fibonacci(n)` that calculates the nth Fibonacci number using a loop with a time complexity of O(n). If n is negative, return -1. Otherwise, return the nth Fibonacci number, where the Fibonacci sequence is defined as fib(0) = 0, fib(1) = 1, and fib(n) = fib(n-1) + fib(n-2) for n > 1.
"""

def fibonacci(n):
    if n < 0:
        return -1  # Return -1 for invalid inputs
    
    if n <= 1:
        return n  # Return n for n = 0 or n = 1
    
    # Initialize variables to store the two previous Fibonacci numbers
    fib_n_minus_2 = 0
    fib_n_minus_1 = 1
    
    # Calculate the nth Fibonacci number iteratively
    for _ in range(2, n+1):
        fib_n = fib_n_minus_2 + fib_n_minus_1
        
        # Update the two previous Fibonacci numbers
        fib_n_minus_2 = fib_n_minus_1
        fib_n_minus_1 = fib_n
    
    return fib_n