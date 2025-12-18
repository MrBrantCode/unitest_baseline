"""
QUESTION:
Write a Python function named `filter_strings` that takes a list of strings (`my_list`) and a character as input. The function should return a list of strings that start and end with the given character. The returned strings should be in uppercase and the list should be in reverse order.
"""

def filter_strings(my_list, character):
    """
    This function filters a list of strings based on a given character.
    It returns a list of strings that start and end with the character, 
    in uppercase and in reverse order.

    Args:
        my_list (list): A list of strings.
        character (str): A character to filter the strings.

    Returns:
        list: A list of filtered strings.
    """
    return [string.upper() for string in my_list if string[0] == character and string[-1] == character][::-1]