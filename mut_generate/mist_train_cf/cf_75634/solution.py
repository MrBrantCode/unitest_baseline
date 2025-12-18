"""
QUESTION:
Implement a function named `fibonacci_recursive` that takes an integer `n` as input and returns the nth Fibonacci number, where the Fibonacci sequence starts with 0 and 1. Use a while loop to generate the Fibonacci sequence from the 5th term down to the 0th term in reverse order.
"""

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2))