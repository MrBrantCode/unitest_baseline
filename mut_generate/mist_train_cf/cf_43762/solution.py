"""
QUESTION:
Create a function called `filter_odd_values` that takes a list of tuples as input, where each tuple contains a key-value pair. The function should return a dictionary where the key-value pairs are the input tuples, but with a condition to exclude any tuples with odd values.
"""

def filter_odd_values(input_list):
    """Return a dictionary from input list of tuples, excluding tuples with odd values."""
    return {k: v for (k, v) in input_list if v % 2 == 0}