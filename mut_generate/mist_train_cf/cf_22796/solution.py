"""
QUESTION:
Create a function called `find_max_values` that takes a 2D list of integers as input. For each sublist in the input list, find the maximum value and return it if the maximum value is greater than 10. If no value in the sublist is greater than 10, return "None" for that sublist.
"""

def find_max_values(data):
    """
    For each sublist in the input list, find the maximum value and return it if the maximum value is greater than 10.
    If no value in the sublist is greater than 10, return "None" for that sublist.

    Args:
        data (list): A 2D list of integers.

    Returns:
        list: A list containing the maximum values from each sublist if greater than 10, otherwise "None".
    """
    max_values = []
    for sublist in data:
        max_value = max(sublist) if max(sublist) > 10 else None
        max_values.append(max_value)
    return max_values