"""
QUESTION:
Write a function `reorder_unique` that takes an array of integers as input, removes duplicate elements, and returns the resulting array in decreasing order without modifying the original array.
"""

def reorder_unique(nums):
    return sorted(list(set(nums)), reverse=True)