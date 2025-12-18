"""
QUESTION:
Write a function named `sum_numbers` that uses recursion to calculate the sum of numbers from 0 to n (inclusive). The function should take one integer parameter `n` and return the sum of all integers from 0 to `n`.
"""

def sum_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_numbers(n-1)