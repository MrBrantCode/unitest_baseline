"""
QUESTION:
Write a function `get_unique_values_descending` that takes a list of integers as input and returns a list of unique integers in descending order. The input list can contain both positive and negative numbers, and may have duplicate values.
"""

def get_unique_values_descending(numbers):
    unique_values = list(set(numbers))
    unique_values.sort(reverse=True)
    return unique_values