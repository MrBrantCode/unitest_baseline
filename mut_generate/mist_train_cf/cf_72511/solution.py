"""
QUESTION:
Write a function called `convert_to_title_case` that takes a string as input and returns the string with the first character of each word converted to uppercase, without using any built-in string title case conversion functions.
"""

def convert_to_title_case(input_string):
    """
    Converts the first character of each word in a string to uppercase.

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: The string with the first character of each word converted to uppercase.
    """
    result = ''
    capitalize_next = True
    for char in input_string:
        if char.isspace():
            result += char
            capitalize_next = True
        elif capitalize_next:
            result += char.upper()
            capitalize_next = False
        else:
            result += char
    return result