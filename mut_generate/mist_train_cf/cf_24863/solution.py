"""
QUESTION:
Write a function named `sum_numbers` that calculates the sum of integers from 0 to n (inclusive) efficiently. The function should take one integer parameter `n` and return the calculated sum. The function should use the mathematical formula for the sum of an arithmetic series to achieve optimal performance.
"""

def sum_numbers(n):
    return n * (n + 1) // 2