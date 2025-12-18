"""
QUESTION:
Create a function `get_positive_and_sort` that takes a list of integers as input and returns a new list containing only the positive numbers from the original list, sorted in ascending order. The function should not modify the original list.
"""

def get_positive_and_sort(l: list):
    """Return only positive numbers in the list, sorted in ascending order."""
    return sorted([num for num in l if num > 0])