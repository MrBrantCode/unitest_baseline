"""
QUESTION:
Write a function called `factorial(n)` that calculates the factorial of a non-negative integer `n`. Implement the function iteratively, not recursively, and optimize it to have a time complexity of O(n). The function should return `None` for negative input numbers.
"""

def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result