"""
QUESTION:
Write a function `max_difference(arr)` that takes a list of integers `arr` as input and returns the maximum difference between any two numbers in the list. The function should be able to handle lists with at least two elements.
"""

def max_difference(arr):
    return max(arr) - min(arr)