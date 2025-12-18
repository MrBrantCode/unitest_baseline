"""
QUESTION:
Design a recursive function `fibonacci(n)` that calculates the Fibonacci sequence up to a given index `n`. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. Implement the function such that it handles cases where `n` is 0 or 1.
"""

def fibonacci(n):
    if n <= 1:
        return n
    else: 
        return fibonacci(n-1) + fibonacci(n-2)