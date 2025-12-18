"""
QUESTION:
Write a recursive function `factorial(n)` to calculate the factorial of a given integer `n`. The function should handle cases where `n` is negative and return `None` in such cases. The time complexity of the function should be O(n).
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    if n < 0:
        return None
    return n * factorial(n-1)