"""
QUESTION:
Write a function `sortStrings` that takes a list of strings `arr` as input, where `arr` contains only lowercase alphabets, has no leading or trailing spaces, and does not contain empty strings. Sort the strings in ascending order based on the number of distinct characters in each string. If two or more strings have the same number of distinct characters, sort them lexicographically. The function should return a list of sorted strings with no duplicates. The input array `arr` can contain up to 10^5 strings, and each string can have a maximum length of 10^3.
"""

def sortStrings(arr):
    """
    Sorts a list of strings based on the number of distinct characters in each string.
    If two or more strings have the same number of distinct characters, they are sorted lexicographically.
    The function returns a list of sorted strings with no duplicates.

    Args:
        arr (list): A list of strings containing only lowercase alphabets.

    Returns:
        list: A list of sorted strings with no duplicates.
    """
    # Use a set to store unique strings
    unique_strings = set(arr)
    
    # Sort the strings based on the number of distinct characters and lexicographical order
    sorted_strings = sorted(unique_strings, key=lambda s: (len(set(s)), s))
    
    return sorted_strings