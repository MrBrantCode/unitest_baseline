"""
QUESTION:
Write a function `fibonacci_seq(n)` that calculates the nth Fibonacci number, handling inputs up to 5000. The function should validate the input, handle errors, and optimize for large values of n. Implement a solution with a time complexity better than O(2^n) and efficient memory usage.
"""

def fibonacci_seq(n, computed = {0: 0, 1: 1}):
    if n < 0:
        return "Incorrect input. Please enter a non-negative number."
    if n not in computed:
        computed[n] = fibonacci_seq(n-1, computed) + fibonacci_seq(n-2, computed)
    return computed[n]