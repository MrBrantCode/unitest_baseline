"""
QUESTION:
Create a function `convert_list_to_dict` that takes a list of integers as input and returns a dictionary where each key is an element from the list, and each value is a list containing the index of the element in the original list, the square of the element, and the cube of the element.
"""

def convert_list_to_dict(lst):
    """
    Convert a list of integers into a dictionary where each key is an element from the list,
    and each value is a list containing the index of the element in the original list,
    the square of the element, and the cube of the element.

    Args:
        lst (list): A list of integers.

    Returns:
        dict: A dictionary where each key is an element from the list, and each value is a list
              containing the index of the element in the original list, the square of the element,
              and the cube of the element.
    """
    result = {}
    for index, element in enumerate(lst):
        result[element] = [index, element**2, element**3]
    return result