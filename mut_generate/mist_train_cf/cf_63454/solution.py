"""
QUESTION:
Write a function named `find_last_pair` that takes a list of uneven numerical values as input and returns the last pair of entities in the list. The function should work for any list length, but assume the list will always have at least two elements.
"""

def find_last_pair(numbers):
    """
    Returns the last pair of entities in a list of numbers.

    Args:
    numbers (list): A list of numbers.

    Returns:
    list: The last pair of entities in the input list.
    """
    return numbers[-2:]