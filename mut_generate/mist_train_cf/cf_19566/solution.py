"""
QUESTION:
Create a function `factorial(n)` that calculates the factorial of a given positive integer `n` with a time complexity of O(n). The function should return an error message if `n` is not a positive integer.
"""

def entance(n):
    if not isinstance(n, int) or n < 0:
        return "Error: Input must be a positive integer."

    if n == 0 or n == 1:
        return 1

    return n * entance(n - 1)