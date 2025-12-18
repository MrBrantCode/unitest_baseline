"""
QUESTION:
Write a function `convert_to_uppercase` that takes a list of strings as input and returns a new list containing the strings in uppercase, excluding any strings that contain numbers or special characters.
"""

def convert_to_uppercase(strings):
    """
    Convert a list of strings to uppercase, excluding any strings that contain numbers or special characters.

    Args:
        strings (list): A list of strings.

    Returns:
        list: A new list containing the strings in uppercase.
    """
    def contains_numbers_or_special_characters(string):
        for char in string:
            if not char.isalpha():
                return True
        return False

    return [string.upper() for string in strings if not contains_numbers_or_special_characters(string)]