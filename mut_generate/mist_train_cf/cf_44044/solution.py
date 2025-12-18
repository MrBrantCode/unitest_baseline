"""
QUESTION:
Write a function named `string_to_list` that transforms a given string into a list. The function should take a string `input_str` and an optional string `separator` as input. If the `separator` is not provided, the function should split the string into a list of individual characters. If the `separator` is provided, the function should split the string into a list of words using the `separator` as the delimiter. The function should return the resulting list.
"""

def string_to_list(input_str, separator=None):
    """
    This function transforms a given string into a list.
    
    Args:
    input_str (str): The input string to be converted into a list.
    separator (str): The separator to split the string. Defaults to None.
    
    Returns:
    list: A list of characters or words depending on the separator provided.
    """
    if separator is None:
        return list(input_str)
    else:
        return input_str.split(separator)