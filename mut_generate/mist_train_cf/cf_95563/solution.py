"""
QUESTION:
Implement a recursive function named `factorial(n)` to calculate the factorial of a positive integer number `n`. The function should return an error message if `n` is negative and handle edge cases where `n` is zero. The function should have a time complexity of O(n) and space complexity of O(1) to efficiently handle large inputs.
"""

def factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)