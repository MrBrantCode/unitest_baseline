"""
QUESTION:
Create a function called `sort_strings` that takes a list of strings as input and returns a new list containing the input strings in alphabetical order. The function should meet the following requirements: 

- The sorting algorithm should have a time complexity of O(n log n).
- The space complexity should be O(n).
- The sorting should be case-insensitive.
- The function should remove any duplicate strings from the list before sorting.
- The sorting should be stable.
- The function should be able to handle non-alphanumeric characters in the strings.
"""

def sort_strings(list_of_strings):
    """
    Sorts a list of strings in alphabetical order, removes duplicates, and performs case-insensitive sorting.

    Args:
    list_of_strings (list): A list of strings.

    Returns:
    list: A new list containing the input strings in alphabetical order.
    """
    return sorted(list(set(list_of_strings)), key=lambda s: s.lower())