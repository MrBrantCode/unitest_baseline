"""
QUESTION:
Write a function `sort_strings_mixed_list(mixed_list)` that takes a list containing a mix of integers and strings as input. The function should return a new list with the integers remaining in their original positions, while the strings are sorted in lexicographic order. The input list can contain any number of integers and strings. The function should not modify the original list.
"""

def sort_strings_mixed_list(mixed_list):
    """
    This function takes a list containing a mix of integers and strings as input.
    It returns a new list with the integers remaining in their original positions, 
    while the strings are sorted in lexicographic order.

    Args:
        mixed_list (list): A list containing a mix of integers and strings.

    Returns:
        list: A new list with sorted strings and unchanged integer positions.
    """

    # separate integers and strings using filter()
    str_list = sorted([x for x in mixed_list if isinstance(x, str)])

    # initialize an empty result list
    result = []

    # initialize string index
    str_index = 0

    # iterate over the original list
    for item in mixed_list:
        # if item is a string, append the next string from the sorted string list
        if isinstance(item, str):
            result.append(str_list[str_index])
            str_index += 1
        # if item is an integer, append it as is
        else:
            result.append(item)

    return result