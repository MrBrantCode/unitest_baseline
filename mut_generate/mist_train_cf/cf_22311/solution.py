"""
QUESTION:
Create an immutable object in Python with three elements: a string, an integer, and a nested object containing at least two elements. The nested object should be a dictionary, and the entire structure should not be modifiable once created.
"""

def entrance(string, integer, nested_object):
    """
    Creates an immutable object with three elements: a string, an integer, 
    and a nested object containing at least two elements.

    Args:
    string (str): The first element of the immutable object.
    integer (int): The second element of the immutable object.
    nested_object (dict): A dictionary with at least two elements.

    Returns:
    tuple: An immutable object with three elements.
    """
    return (string, integer, tuple(nested_object.items()))