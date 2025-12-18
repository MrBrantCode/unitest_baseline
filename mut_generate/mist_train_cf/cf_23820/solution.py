"""
QUESTION:
Write a function named `generate_fibonacci` that takes an integer `n` as input and returns a list of Fibonacci numbers up to `n` items. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two numbers.
"""

def generate_fibonacci(n):
    """
    Generates a series of Fibonacci numbers up to a certain number of items.
    """
    fib = [0, 1]
 
    if n < 2:
        return fib[:n]
 
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib