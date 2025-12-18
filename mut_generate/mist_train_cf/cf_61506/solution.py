"""
QUESTION:
Write a function `remove_duplicates` that takes a list of integers as input and returns a list of integers where each integer appears only once. The function should not preserve the original order of the integers.
"""

def remove_duplicates(data):
    """Returns a list of integers where each integer appears only once."""
    return list(set(data))