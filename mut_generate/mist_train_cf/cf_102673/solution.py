"""
QUESTION:
Create a function called `delete_items` that takes a list of integers as input and returns a new list with all integers less than or equal to 5 removed.
"""

def delete_items(lst):
    """
    This function takes a list of integers as input and returns a new list with all integers less than or equal to 5 removed.

    Args:
        lst (list): A list of integers.

    Returns:
        list: A new list with all integers less than or equal to 5 removed.
    """
    return [item for item in lst if item > 5]