"""
QUESTION:
Compute the nth Fibonacci number using a recursive approach without using memoization. 

Define a function named `fibonacci` that takes one argument `n`, representing the position of the Fibonacci number to be calculated. The function should use recursive calls to calculate the previous two Fibonacci numbers and sum them up to get the nth Fibonacci number. 

The base case should handle `n` being 0 or 1.
"""

def fibonacci(n):
    # Base case for n = 0 or 1
    if n <= 1:
        return n

    # Recursive case
    return fibonacci(n-1) + fibonacci(n-2)