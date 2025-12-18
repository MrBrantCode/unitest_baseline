"""
QUESTION:
Create a function `filter_list` that takes a list of mixed data types and a list of programming languages as input, and returns a new list containing only the strings from the original list that are either a programming language or have more than 5 characters. The function should ignore non-string items in the original list.
"""

def filter_list(input_list, programming_languages):
    """
    This function filters a list of mixed data types and returns a new list containing only the strings 
    from the original list that are either a programming language or have more than 5 characters.

    Args:
        input_list (list): A list of mixed data types.
        programming_languages (list): A list of programming languages.

    Returns:
        list: A new list containing the filtered strings.
    """

    return [item for item in input_list if isinstance(item, str) and (item in programming_languages or len(item) > 5)]