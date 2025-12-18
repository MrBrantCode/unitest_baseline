"""
QUESTION:
Write a function called `access_first_element` that takes a dictionary as input. The dictionary contains a key that maps to a list. The function should return the first element of the list without modifying the original list.
"""

def access_first_element(data, key):
    """
    Access the first element of the list in a dictionary.

    Args:
    data (dict): The dictionary containing a key that maps to a list.
    key (str): The key that maps to the list in the dictionary.

    Returns:
    The first element of the list.
    """
    return data[key][0]