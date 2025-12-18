"""
QUESTION:
Create a function `filter_list` that takes a list of integers as input, filters the list to include only the numbers that are divisible by both 2 and 3, and returns the filtered list in descending order.
"""

def filter_list(numbers):
    """
    Filters a list of integers to include only numbers divisible by both 2 and 3, 
    and returns the filtered list in descending order.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: The filtered list of integers in descending order.
    """
    return sorted([num for num in numbers if num % 2 == 0 and num % 3 == 0], reverse=True)