"""
QUESTION:
Create a function `access_first_element` that takes a dictionary `data` as input, where the dictionary contains a nested list. The function should return the first element of the nested list without modifying the original list. Assume the key for the nested list in the dictionary is known.
"""

def access_first_element(data, key):
    """
    Access the first element of a nested list in a dictionary.

    Args:
    data (dict): The dictionary containing a nested list.
    key (str): The key for the nested list in the dictionary.

    Returns:
    The first element of the nested list.
    """
    return data[key][0]