"""
QUESTION:
Create a function named `tuple_to_dict` that takes a list of tuples as input, where each tuple contains a unique identifier and a full name. Convert the list of tuples into a dictionary, using the unique identifiers as keys and the full names as values, and return the resulting dictionary.
"""

def tuple_to_dict(tuples_list):
    """
    Converts a list of tuples into a dictionary, 
    using the unique identifiers as keys and the full names as values.

    Args:
        tuples_list (list): A list of tuples containing unique identifiers and full names.

    Returns:
        dict: A dictionary with unique identifiers as keys and full names as values.
    """
    return dict((y, x) for x, y in tuples_list)