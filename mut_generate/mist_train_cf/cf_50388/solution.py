"""
QUESTION:
Implement a function `fibonacci(n)` that generates the nth Fibonacci number using an efficient algorithm with a computational complexity of O(n). The Fibonacci sequence is defined as F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1. The input `n` should be a non-negative integer.
"""

def fibonacci(n):
    # Check if n is negative
    if n < 0:
        return "Input should be a positive integer."

    # Check if n is 0 or 1, Fibonacci is the same as n in these cases
    elif n == 0 or n == 1:
        return n

    # Create an empty array of size n+1
    fib = [0]*(n+1)

    # Set initial conditions
    fib[1] = 1

    # Generate Fibonacci numbers
    for i in range(2 , n+1):
        fib[i] = fib[i-1] + fib[i-2]

    # return the requested fibonacci number
    return fib[n]