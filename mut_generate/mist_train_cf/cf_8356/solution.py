"""
QUESTION:
Write a recursive function named `factorial` that takes a positive integer `n` and an optional dictionary `memo` to calculate the factorial of `n`. The function should return an error message if `n` is not a positive integer. The function should use memoization to optimize performance. The time and space complexities should be considered.
"""

def factorial(n, memo={}):
    # Check if n is a positive integer
    if not isinstance(n, int) or n < 0:
        return "Invalid input. Please enter a positive integer."

    # Check if n is already calculated
    if n in memo:
        return memo[n]

    # Base case: factorial of 0 is 1
    if n == 0:
        return 1

    # Recursive case: calculate factorial using memoization
    result = n * factorial(n-1, memo)
    memo[n] = result
    return result