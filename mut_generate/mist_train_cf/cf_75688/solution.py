"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given non-negative integer `n` using recursion with memoization. The function should be able to handle inputs up to 1000 effectively. The solution should use a dictionary to store already calculated factorials to reduce computation time.
"""

# Initialize a dictionary for memoization
memo = {0: 1, 1: 1}

def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # If n is present in the memo dictionary, return its value
    elif n in memo:
        return memo[n]
    # If n is not present in the memo dictionary, calculate its factorial
    else:
        memo[n] = n * factorial(n-1)
        return memo[n]