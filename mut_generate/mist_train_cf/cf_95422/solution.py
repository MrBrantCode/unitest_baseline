"""
QUESTION:
Create a function named `remove_duplicates` that takes an array of integers as input, removes duplicates, and returns a tuple containing the array of unique elements in ascending order and the count of unique elements. The function should handle empty arrays, arrays with a single element, negative numbers, and floating-point numbers (which should be rounded to the nearest integer).
"""

def remove_duplicates(arr):
    """
    Removes duplicates from an array, rounds floating-point numbers to the nearest integer,
    and returns a tuple containing the array of unique elements in ascending order and the count of unique elements.

    Args:
        arr (list): The input array of integers.

    Returns:
        tuple: A tuple containing the array of unique elements in ascending order and the count of unique elements.
    """
    if len(arr) == 0:
        return [], 0
    elif len(arr) == 1:
        return arr, 1
    unique_elements = set()
    for num in arr:
        unique_elements.add(round(num))
    unique_array = list(unique_elements)
    unique_array.sort()
    return unique_array, len(unique_array)