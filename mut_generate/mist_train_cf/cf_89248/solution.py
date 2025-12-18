"""
QUESTION:
Design a recursive function named `fibonacci` that takes an integer `n` and returns the `n`th Fibonacci number. The function should have a time complexity of O(n) and a space complexity of O(n). It should handle negative input values by returning an error message and implement memoization to optimize recursive calls without using any loops or iteration constructs.
"""

def fibonacci(n, memo={}):
    # Check for negative input values
    if n < 0:
        return "Error: Negative input value"

    # Check if n is already in the memoization table
    if n in memo:
        return memo[n]

    # Base cases for Fibonacci sequence
    if n == 0:
        memo[n] = 0
        return 0
    elif n == 1:
        memo[n] = 1
        return 1

    # Recursive calls to calculate the n'th Fibonacci number
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]