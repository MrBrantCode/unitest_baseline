"""
QUESTION:
Write a function `remove_duplicates` that takes a list of mixed data types as input. The list may contain nested lists. Convert the input list to a list of tuples, treating nested lists as tuples, and then remove any duplicate tuples. The order of the elements in the original list may not be preserved. Note that nested lists are considered distinct if they have the same elements in a different order.
"""

def remove_duplicates(input_list):
    """
    Removes duplicates from a list containing mixed data types, including nested lists.
    The order of elements may not be preserved.

    Args:
        input_list (list): A list of mixed data types.

    Returns:
        list: A list of tuples with duplicates removed.
    """
    input_list = [tuple(x) if isinstance(x, list) else x for x in input_list]
    input_list = list(set(input_list))
    return input_list