"""
QUESTION:
Implement a tail-recursive function `fibonacci(n)` that returns the nth number in the Fibonacci sequence. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. If n is less than or equal to 1, return n.
"""

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)