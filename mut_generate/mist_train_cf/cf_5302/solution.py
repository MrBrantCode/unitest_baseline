"""
QUESTION:
Write a function `filter_strings` that takes a list of strings as input and returns a list of strings that contain at least two occurrences of the letter 'a' and end with the letter 'e'. The returned list should be sorted in descending order based on the number of occurrences of the letter 'a' in each string.
"""

def filter_strings(strings):
    """
    Filters a list of strings and returns a list of strings that contain at least two occurrences of the letter 'a' and end with the letter 'e'.
    The returned list is sorted in descending order based on the number of occurrences of the letter 'a' in each string.

    Args:
        strings (list): A list of strings to filter.

    Returns:
        list: A list of filtered strings.
    """
    return sorted([string for string in strings if string.count('a') >= 2 and string.endswith('e')], key=lambda x: x.count('a'), reverse=True)