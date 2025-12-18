"""
QUESTION:
Create a function called custom_sort that takes a list of strings as input and returns the list sorted in reverse alphabetical order, first by the length of each string in descending order, and then alphabetically within strings of the same length. The input list is not guaranteed to be non-empty and the function must work for any list of strings.
"""

def custom_sort(lst):
    """
    Sorts a list of strings in reverse alphabetical order, 
    first by the length of each string in descending order, 
    and then alphabetically within strings of the same length.

    Args:
        lst (list): A list of strings.

    Returns:
        list: The sorted list of strings.
    """
    return sorted(lst, key=lambda x: (-len(x), x[::-1]))