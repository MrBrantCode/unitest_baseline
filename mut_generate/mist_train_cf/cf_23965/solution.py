"""
QUESTION:
Create a function `remove_zeros` that takes an array of integers as input and returns a new array with all elements with the value 0 removed.
"""

def remove_zeros(arr):
    return [item for item in arr if item != 0]