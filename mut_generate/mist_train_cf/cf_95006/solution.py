"""
QUESTION:
Create a function `custom_sort` that takes a list of tuples, where each tuple contains a string and an integer. The function should sort the list in descending order of the integer values. If multiple tuples have the same integer value, they should be sorted in descending order of the string values.
"""

def custom_sort(tuples_list):
    """
    Sorts a list of tuples in descending order of integer values.
    If multiple tuples have the same integer value, they are sorted in descending order of string values.

    Args:
        tuples_list (list): A list of tuples, where each tuple contains a string and an integer.

    Returns:
        list: The sorted list of tuples.
    """
    return sorted(tuples_list, key=lambda x: (-x[1], x[0].lower()[::-1]))