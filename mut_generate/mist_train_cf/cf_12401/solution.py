"""
QUESTION:
Write a function named `remove_duplicates_and_sort` that takes a string as input and returns a new string with all duplicate characters removed and the remaining characters sorted in ascending order. The input string may contain any characters, including letters and symbols, and is not guaranteed to be in any specific order. The function should return a string of unique characters, sorted in ascending order.
"""

def remove_duplicates_and_sort(input_string):
    """
    Removes duplicate characters from the input string and returns a new string 
    with the remaining characters sorted in ascending order.

    Args:
        input_string (str): The input string.

    Returns:
        str: A string of unique characters, sorted in ascending order.
    """
    # Remove duplicate characters
    unique_chars = set(input_string)

    # Sort the remaining characters in ascending order
    sorted_chars = sorted(unique_chars)

    # Convert the sorted characters back to a string
    return ''.join(sorted_chars)