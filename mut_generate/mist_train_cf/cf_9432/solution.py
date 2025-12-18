"""
QUESTION:
Create a function named `convert_to_sorted_string` that takes a list of integers as input and returns a comma-separated string of the input numbers in ascending order.
"""

def convert_to_sorted_string(lst):
    return ','.join(map(str, sorted(lst)))