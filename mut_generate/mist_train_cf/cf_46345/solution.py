"""
QUESTION:
Create a function named `transform_list_to_dict` that transforms a given list into a dictionary while maintaining the original values. The list does not have explicit keys, so the function should use the index of each element as a key.
"""

def transform_list_to_dict(lst):
    """
    This function transforms a given list into a dictionary while maintaining the original values.
    The list does not have explicit keys, so the function uses the index of each element as a key.

    Args:
        lst (list): The list to be transformed into a dictionary.

    Returns:
        dict: A dictionary with the index of each element in the list as keys.
    """
    return {k: v for k, v in enumerate(lst)}