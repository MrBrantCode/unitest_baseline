"""
QUESTION:
Create a function named `fib(n)` that calculates the n-th Fibonacci number recursively. Implement error handling to check if the input `n` is a non-negative integer. If `n` is not an integer or is negative, return an error message. Optimize the function using memoization to minimize complexity and ensure it can handle large values of `n` efficiently.
"""

def fib(n, memo = {}):
    # Error handling for non-integer values
    if not isinstance(n, int):
        return "Error: Input must be an integer."
    # Error handling for negative integers
    if n < 0:
        return "Error: Input must be a positive integer."
    # Base cases for the Fibonacci sequence
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Memoization to improve efficiency 
    elif n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]