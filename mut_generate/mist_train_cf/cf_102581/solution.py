"""
QUESTION:
Write a function `concatenate_list` that takes a list of strings and a separator as input, and returns a string that is the concatenation of all elements in the list, separated by the given separator. The separator must be a single, non-alphanumeric character.
"""

def concatenate_list(input_list, separator):
    """
    Concatenates a list of strings into a single string separated by a given separator.

    Args:
        input_list (list): A list of strings to be concatenated.
        separator (str): A single, non-alphanumeric character to separate the strings.

    Returns:
        str: The concatenated string.
    """
    return separator.join(input_list)