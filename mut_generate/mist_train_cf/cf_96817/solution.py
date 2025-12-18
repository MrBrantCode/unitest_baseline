"""
QUESTION:
Write a function `calculate_combination(n, k, limit)` that calculates the combination of n elements taken k at a time. The function should return an error message if n is smaller than k or if the calculated combination exceeds the limit. The inputs n and k are non-negative integers, and the limit is a positive integer.
"""

import math

def calculate_combination(n, k, limit):
    # Check if n is smaller than k
    if n < k:
        return "Error: n must be greater than or equal to k."

    # Calculate the combination
    combination = math.comb(n, k)

    # Check if the calculated combination exceeds the limit
    if combination > limit:
        return f"Error: The calculated combination exceeds the limit of {limit}."

    return combination