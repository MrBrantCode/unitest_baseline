"""
QUESTION:
Implement the `factorial` function that takes a non-negative integer `n` as input and returns the factorial of `n`. The function should handle the base case where `n` is 0 or 1, and also account for larger values of `n`.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result