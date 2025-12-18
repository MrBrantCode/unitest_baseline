"""
QUESTION:
Write a function named `factorial(n)` that calculates the factorial of a positive integer `n` using recursion. The input integer `n` should be between 1 and 10 (inclusive). If `n` is not a positive integer or is greater than 10, the function should return an error message. The time complexity of the function should be O(n).
"""

def factorial(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        return "Error: Input must be a positive integer"
    # Check if n is greater than 10
    if n > 10:
        return "Error: Input must be less than or equal to 10"
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: factorial of n is n multiplied by factorial of (n-1)
    return n * factorial(n-1)