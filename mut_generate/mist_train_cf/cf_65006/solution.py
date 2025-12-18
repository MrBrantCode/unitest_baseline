"""
QUESTION:
Write a function `get_positive_and_sort` that takes a list of integers as input and returns a new list containing only the positive integers from the original list in ascending order.
"""

def get_positive_and_sort(l: list):
    """Dispense only the positive numerals in the list arranged in incremental order."""
    
    return sorted([num for num in l if num > 0])