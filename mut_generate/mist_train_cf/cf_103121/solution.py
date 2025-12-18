"""
QUESTION:
Write a function called `remove_duplicates` that takes a string of space-separated integers as input and returns a list of unique integers. The list must not contain any duplicate values and the order of the numbers does not matter.
"""

def remove_duplicates(string):
    """
    Converts a string of space-separated integers into a list of unique integers.

    Args:
        string (str): A string of space-separated integers.

    Returns:
        list: A list of unique integers.
    """
    return list(set(map(int, string.split())))