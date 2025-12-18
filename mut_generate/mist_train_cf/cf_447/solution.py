"""
QUESTION:
Write a function called "flatten_list" that takes in a single parameter "lst" (a list) representing the input list. The function should return a new list that is the flattened version of the input list. The input list may contain nested lists, integers, and strings. The flattened list should only include integer values. If any non-integer values are encountered, discard them. If any strings are encountered, attempt to convert them to integers and include them in the flattened list. If any nested lists are encountered, recursively flatten them and include their integer values in the flattened list.
"""

def flatten_list(lst):
    """
    This function takes a list as input, recursively flattens it, 
    and returns a new list containing only the integer values.
    
    If a string is encountered, an attempt is made to convert it to an integer.
    Non-integer values are discarded.

    Args:
        lst (list): The input list to be flattened.

    Returns:
        list: A new list containing only the integer values from the input list.
    """
    flattened_list = []
    for item in lst:
        if isinstance(item, int):
            flattened_list.append(item)
        elif isinstance(item, str):
            try:
                num = int(item)
                flattened_list.append(num)
            except ValueError:
                pass
        elif isinstance(item, list):
            flattened_sublist = flatten_list(item)
            flattened_list.extend(flattened_sublist)
    return flattened_list