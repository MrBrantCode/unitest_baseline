"""
QUESTION:
Create a function named `find_strings` that takes a list of strings as input and returns a list of strings that start and end with the same letter, without modifying the original input list.
"""

def find_strings(input_list):
    """
    Returns a list of strings that start and end with the same letter.

    Args:
        input_list (list): A list of strings.

    Returns:
        list: A list of strings that start and end with the same letter.
    """
    return [string for string in input_list if string[0] == string[-1]]