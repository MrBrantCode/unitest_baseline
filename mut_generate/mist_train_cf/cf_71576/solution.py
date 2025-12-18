"""
QUESTION:
Write a function `ReplaceNumericCharacters` that takes an input string and returns a new string where all numeric characters are replaced with asterisks (`*`).
"""

def replace_numeric_characters(input_string):
    """
    Replaces all numeric characters in a string with asterisks.

    Args:
    input_string (str): The input string to process.

    Returns:
    str: A new string with all numeric characters replaced with asterisks.
    """
    output_string = ''
    for char in input_string:
        if char.isdigit():
            output_string += '*'
        else:
            output_string += char
    return output_string