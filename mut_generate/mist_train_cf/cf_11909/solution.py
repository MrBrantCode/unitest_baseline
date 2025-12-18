"""
QUESTION:
Write a function named "reverse_array_to_string" that takes an array of integers as input and returns a string where the integers are in reverse order, separated by commas.
"""

def reverse_array_to_string(arr):
    return ','.join(map(str, arr[::-1]))