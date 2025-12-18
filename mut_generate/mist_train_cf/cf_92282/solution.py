"""
QUESTION:
Write a function called `remove_duplicates_and_sort` that takes a string as input, removes any duplicate characters, and returns the remaining characters in ascending order as a string.
"""

def remove_duplicates_and_sort(input_string):
    """
    Removes any duplicate characters from the input string and returns the remaining characters in ascending order as a string.

    Args:
        input_string (str): The input string.

    Returns:
        str: The string with duplicate characters removed and sorted in ascending order.
    """
    return ''.join(sorted(set(input_string)))