"""
QUESTION:
Write a recursive function named `factorial` to calculate the factorial of a non-negative integer `n`. The function should handle the base case when `n` equals 0. Analyze the time and space complexity of the recursive solution.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)