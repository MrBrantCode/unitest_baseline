"""
QUESTION:
Create a function named `fibonacci` that calculates the Fibonacci number at a given index using a recursive approach with a time complexity of O(2^n). The function should take one argument, the index `n`, and return the corresponding Fibonacci number.
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)