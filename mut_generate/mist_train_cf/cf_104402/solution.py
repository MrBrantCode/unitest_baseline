"""
QUESTION:
Find the minimum value and its index in a given list of numbers.

Create a function named `find_min_value_and_index` that takes a list of numbers as input and returns the minimum value and its index in the list. The function should iterate through the list to find the minimum value and its index. If the list is empty, the function can return any value that indicates the absence of a minimum value and index.
"""

def find_min_value_and_index(numbers):
    """
    Find the minimum value and its index in a given list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        tuple: A tuple containing the minimum value and its index. If the list is empty, returns (None, None).
    """
    if not numbers:
        return None, None

    min_value = float('inf')
    min_index = -1

    for index, num in enumerate(numbers):
        if num < min_value:
            min_value = num
            min_index = index

    return min_value, min_index