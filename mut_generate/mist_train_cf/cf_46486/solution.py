"""
QUESTION:
Create a function named `lexicographic_sort` that takes a list of strings as input and returns the list sorted in lexicographic sequence. The sorting should be case-insensitive, and special characters and numbers should be sorted according to their ASCII values. The original case of the strings should be preserved in the sorted output, with the original order of strings that are identical except for case maintained if they appear so in the original list.
"""

def lexicographic_sort(list_of_strings):
    """
    Sorts a list of strings in lexicographic sequence, ignoring case.
    Preserves the original case of strings and order of strings that are identical except for case.

    Args:
        list_of_strings (list): A list of strings to sort.

    Returns:
        list: The sorted list of strings.
    """
    return sorted(list_of_strings, key=lambda s: (s.lower(), s))