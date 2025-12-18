"""
QUESTION:
Write a function called `split_and_sort` that takes a string of at least 5 words separated by hyphens as input. The function should split the string into an array using the hyphen as a delimiter and return the resulting array in reverse alphabetical order.
"""

def split_and_sort(input_str):
    """
    This function splits a string into an array using the hyphen as a delimiter 
    and returns the resulting array in reverse alphabetical order.

    Args:
        input_str (str): A string of at least 5 words separated by hyphens.

    Returns:
        list: The resulting array in reverse alphabetical order.
    """
    return sorted(input_str.split("-"), reverse=True)