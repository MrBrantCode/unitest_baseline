"""
QUESTION:
Write a function named `fibonacci` that generates the n-th Fibonacci number using recursion and memoization. The function should handle large values of n (greater than 10^6) efficiently without causing a stack overflow. The Fibonacci sequence is defined as: F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.
"""

# Dictionary to store previously computed Fibonacci numbers
fib_dict = {0: 0, 1: 1}

def fibonacci(n):
    # Check if Fibonacci number is already computed
    if n not in fib_dict:
        # Recursive call to compute Fibonacci number
        fib_dict[n] = fibonacci(n-1) + fibonacci(n-2)
    
    return fib_dict[n]