"""
QUESTION:
Create a function `weighted_sum(numbers, weights)` that calculates the weighted sum of two lists. The function should take in two lists of integers `numbers` and `weights` of equal length, where `weights` contains prime numbers, and return the weighted sum of the corresponding elements in `numbers` and `weights`.
"""

def weighted_sum(numbers, weights):
    return sum(n * w for n, w in zip(numbers, weights))