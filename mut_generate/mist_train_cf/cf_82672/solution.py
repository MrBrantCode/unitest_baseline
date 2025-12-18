"""
QUESTION:
Write a function `sum_of_natural_numbers(N)` that calculates the sum of the first N natural numbers, where N is an integer between 1 and 1,000,000 (inclusive). The solution must have a time complexity better than O(N).
"""

def sum_of_natural_numbers(N):
    return N * (N + 1) // 2