"""
QUESTION:
Create a function called `get_unique_values_descending` that takes a list of integers as input, removes duplicates, and returns the unique integers in descending order. The input list can contain both positive and negative numbers.
"""

def get_unique_values_descending(numbers):
    """
    Removes duplicates from a list of integers and returns the unique integers in descending order.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A list of unique integers in descending order.
    """
    unique_values = list(set(numbers))
    unique_values.sort(reverse=True)
    return unique_values