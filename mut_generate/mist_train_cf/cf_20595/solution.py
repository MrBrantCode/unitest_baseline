"""
QUESTION:
Write a function `sort_strings` that takes a list of strings as input, removes duplicates, sorts the strings in alphabetical order (case-insensitive), and returns the sorted list. The function should have a time complexity of O(n log n) and a space complexity of O(n). The sorting should be stable and handle non-alphanumeric characters in the strings.
"""

def sort_strings(list_of_strings):
    """
    Removes duplicates from the input list of strings, sorts them in alphabetical order (case-insensitive),
    and returns the sorted list.

    Time complexity: O(n log n)
    Space complexity: O(n)

    Args:
        list_of_strings (list): A list of strings

    Returns:
        list: A sorted list of unique strings
    """
    return sorted(set(list_of_strings), key=str.lower)