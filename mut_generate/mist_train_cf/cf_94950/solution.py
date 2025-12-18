"""
QUESTION:
Implement a function named `factorial` that takes a single argument `n` and returns its factorial. The function should use recursion and have a time complexity of O(n). It must handle inputs where `n` is not a positive integer (including negative integers and non-integer values) and return an error message. The function should also handle cases where `n` is greater than 10 and return an error message.
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