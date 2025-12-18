"""
QUESTION:
Write a function `factorial(n)` to calculate the factorial of a given non-negative integer `n` using recursion, with a time complexity of O(n) and a space complexity of O(n).
"""

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: factorial of n is n multiplied by factorial of (n-1)
    return n * factorial(n-1)