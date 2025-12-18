"""
QUESTION:
Write a function `sort_tuples` that takes a list of tuples as input. Each tuple contains two elements: a character and its corresponding occurrence count. The function should sort the list in ascending order based on the occurrence count. If two tuples have the same occurrence count, they should be sorted in descending order based on the character.
"""

def sort_tuples(tuples_list):
    """
    Sorts a list of tuples in ascending order based on the occurrence count.
    If two tuples have the same occurrence count, they are sorted in descending order based on the character.

    Args:
        tuples_list (list): A list of tuples containing a character and its occurrence count.

    Returns:
        list: The sorted list of tuples.
    """
    return sorted(tuples_list, key=lambda x: (x[1], -ord(x[0])))