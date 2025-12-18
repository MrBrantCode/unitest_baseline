"""
QUESTION:
Create a function called `sort_strings` that takes a list of strings as input, sorts the list in ascending order based on the length of each string, maintains the relative order of strings with the same length, and ignores strings containing the letter "e" in the sorting process, placing them last in the sorted list.
"""

def sort_strings(strings):
    """
    Sorts a list of strings based on their length, ignoring strings containing 'e'.

    Args:
        strings (list): A list of strings.

    Returns:
        list: A sorted list of strings.
    """
    return sorted(strings, key=lambda x: (len(x), x) if 'e' not in x else (float('inf'), x))