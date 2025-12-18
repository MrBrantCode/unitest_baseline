"""
QUESTION:
Create a function named `filter_and_sort_uppercase_strings` that takes a list of strings as input, filters out the strings containing only uppercase letters, and returns a new list sorted in descending order by the length of each string, without modifying the original list.
"""

def filter_and_sort_uppercase_strings(arr):
    """
    This function filters out the strings containing only uppercase letters 
    from the input list and returns a new list sorted in descending order 
    by the length of each string.

    Args:
        arr (list): A list of strings.

    Returns:
        list: A list of uppercase strings sorted in descending order by length.
    """
    return sorted([string for string in arr if string.isupper()], key=len, reverse=True)