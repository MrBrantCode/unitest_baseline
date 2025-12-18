"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a non-negative integer `n` using recursion with a time complexity of O(n). The function should return `None` and display an error message if `n` is not a non-negative integer.
"""

def entance(n):
    if not isinstance(n, int) or n < 0:
        print("Error: Input must be a non-negative integer.")
        return None
    if n == 0:
        return 1
    return n * entance(n-1)