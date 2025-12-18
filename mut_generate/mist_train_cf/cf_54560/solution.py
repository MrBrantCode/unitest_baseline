"""
QUESTION:
Write a function `filter_greater_than_10` that takes a list of integers as input and returns a new list containing only the integers greater than 10. The function should use list comprehension.
"""

def filter_greater_than_10(range_array):
    return [i for i in range_array if i > 10]