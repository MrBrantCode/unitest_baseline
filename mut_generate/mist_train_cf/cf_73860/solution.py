"""
QUESTION:
Create a function called `smallest_positive_no_compare` that takes a list of integers as input and returns the smallest positive number in the list without using any comparative functions. If no positive number is found in the list, the function should return `None`.
"""

def smallest_positive_no_compare(lst: list):
    """Return the least positive number in dataset lst without the use of comparative functions.
    Handles both negative and positive numbers within datasets."""
    smallest = float('inf')
    for i in lst:
        if i <= 0:
            continue
        if smallest - i > 0:
            smallest = i
    return smallest if smallest != float('inf') else None