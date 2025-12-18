"""
QUESTION:
Implement a function called `fibonacci(n)` that generates a sequence using the rule F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1. The function should be able to handle inputs up to n = 100 and should be optimized for time complexity.
"""

def fibonacci(n):
    fib = [0, 1]  # List to store Fibonacci numbers
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])  # Calculate Fibonacci number using the rule

    return fib