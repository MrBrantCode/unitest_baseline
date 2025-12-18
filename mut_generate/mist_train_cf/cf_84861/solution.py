"""
QUESTION:
Write a function `reverse_and_lower` that takes an array of strings as input. The function should return a new array where the order of the elements is reversed and all characters within each string are converted to lowercase.
"""

def reverse_and_lower(arr):
    """
    Reverses the order of elements in the array and converts all characters to lowercase.

    Args:
    arr (list): A list of strings.

    Returns:
    list: A new list with the order of elements reversed and all characters in lowercase.
    """
    return [string.lower() for string in arr[::-1]]