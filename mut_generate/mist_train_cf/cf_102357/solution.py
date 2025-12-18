"""
QUESTION:
Write a function named `count_unique_positive_elements` that takes a list of integers as input and returns the number of unique positive elements in the list. The input list is not guaranteed to be sorted.
"""

def count_unique_positive_elements(arr):
    unique_elements = set(filter(lambda x: x > 0, arr))
    return len(unique_elements)