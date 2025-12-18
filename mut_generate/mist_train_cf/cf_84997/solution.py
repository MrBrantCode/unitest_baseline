"""
QUESTION:
Design a recursive function named `fibonacci` that calculates the nth Fibonacci number, where `n` is a non-negative integer. Implement memoization to optimize the function and return an error message for negative input values.
"""

def fibonacci(n, memo = {}):
    # error checking for negative values
    if n < 0:
        return "Error: Negative values are not allowed."
    # base case
    elif n <= 1:
        return n
    # checking if computed Fibonacci number is already in memo
    elif n in memo:
        return memo[n]
    else: # recursive case
        # computing and storing the Fibonacci number in memo
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        return memo[n]