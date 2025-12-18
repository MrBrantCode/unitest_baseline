"""
QUESTION:
Write a function named `generate_positive_array` that takes an array of integers as input and returns a new array containing only the positive integers from the input array.
"""

def generate_positive_array(arr):
    # Use list comprehension to filter out non-positive integers
    return [i for i in arr if i > 0]