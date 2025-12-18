"""
QUESTION:
Write a function named `fibonacci` to calculate the nth Fibonacci number using recursion and memoization, where the function takes two parameters: `n` (the position of the Fibonacci number to be calculated) and `memo` (an optional dictionary for memoization with a default value of an empty dictionary). The function should return the nth Fibonacci number.
"""

def fibonacci(n, memo={}):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Check if result for current value of n is already memoized
    if n in memo:
        return memo[n]

    # Calculate and memoize the result
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]