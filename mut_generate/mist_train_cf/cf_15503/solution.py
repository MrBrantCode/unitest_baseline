"""
QUESTION:
Write a function `flatten_list(lst)` that takes a nested list as input. The function should return a new list containing only integer values from the input list. Non-integer values should be discarded unless they are strings, which should be attempted to be converted to integers. If the conversion is successful, the integer should be included in the output list. If the conversion fails, the string should be discarded. The function should recursively handle nested lists.
"""

def flatten_list(lst):
    """
    This function takes a nested list as input, extracts integer values, 
    and attempts to convert string values to integers. It recursively 
    handles nested lists and discards non-integer values.

    Args:
    lst (list): A nested list containing integer and string values.

    Returns:
    list: A new list containing extracted integer values.
    """
    flattened = []
    for item in lst:
        if isinstance(item, int):
            flattened.append(item)
        elif isinstance(item, str):
            try:
                flattened.append(int(item))
            except ValueError:
                continue
        elif isinstance(item, list):
            flattened.extend(flatten_list(item))
    return flattened