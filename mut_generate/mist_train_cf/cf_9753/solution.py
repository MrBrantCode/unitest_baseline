"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given number `n` using memoization, efficiently handling large numbers up to 10^6. The function should return the calculated factorial.
"""

def factorial(n, memo = {}):
    # Check if factorial is already calculated
    if n in memo:
        return memo[n]

    # Base case for recursion
    if n == 0:
        return 1

    # Calculate factorial
    result = n * factorial(n-1, memo)

    # Store the result in memo dictionary
    memo[n] = result

    return result