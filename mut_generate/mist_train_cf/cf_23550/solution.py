"""
QUESTION:
Write a function, `modify_list`, that takes a list as input, creates a new variable that references the same list, modifies the first element of the original list, and returns the referenced list. The function should return the modified list without creating a copy of the original list.

Note: The input list will always have at least one element.
"""

def modify_list(input_list):
    """
    This function takes a list as input, modifies the first element of the list, 
    and returns the modified list.

    Args:
    input_list (list): The input list to be modified.

    Returns:
    list: The modified list.
    """
    input_list[0] = 'a'
    return input_list