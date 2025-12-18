"""
QUESTION:
Write a function `sort_strings` that takes an array of strings as input and returns the array sorted in ascending order based on the number of distinct characters in each string. If two or more strings have the same number of distinct characters, they should be sorted lexicographically.
"""

def sort_strings(arr):
    """
    Sorts an array of strings based on the number of distinct characters in each string.
    If two or more strings have the same number of distinct characters, they are sorted lexicographically.

    Args:
        arr (list): A list of strings.

    Returns:
        list: The sorted list of strings.
    """
    return sorted(arr, key=lambda x: (len(set(x)), x.lower()))