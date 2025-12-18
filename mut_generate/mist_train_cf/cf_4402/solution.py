"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given non-negative integer `n` using recursion. The function should return an error message if `n` is negative. The function should have a time complexity of O(n) and a space complexity of O(1), excluding the recursion stack.
"""

def factorial(n):
    if n < 0:
        return "Error: Input cannot be negative"
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)