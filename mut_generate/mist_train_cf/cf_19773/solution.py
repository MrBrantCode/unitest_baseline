"""
QUESTION:
Create a function named `create_dict` that takes a list of integers as input and returns a dictionary where each key is an element from the list and its corresponding value is the sum of the indices of all occurrences of the key in the list.
"""

def create_dict(lst):
    """
    This function creates a dictionary where each key is an element from the list 
    and its corresponding value is the sum of the indices of all occurrences of the key in the list.

    Args:
        lst (list): A list of integers.

    Returns:
        dict: A dictionary with keys as elements from the list and values as the sum of indices.
    """
    result_dict = {}
    for i, key in enumerate(lst):
        if key in result_dict:
            result_dict[key] += i
        else:
            result_dict[key] = i
    return result_dict