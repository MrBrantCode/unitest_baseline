"""
QUESTION:
Write a function named `sort_numbers` that takes a list of integers as input, sorts them in descending order, and returns them as a single string without any space. The function should not take any other parameters besides the list of integers.
"""

def sort_numbers(numbers):
    """
    Sorts a list of integers in descending order and returns them as a single string without any space.

    Args:
        numbers (list): A list of integers.

    Returns:
        str: A string containing the sorted numbers without any space.
    """
    numbers.sort(reverse=True)
    return ''.join(map(str, numbers))