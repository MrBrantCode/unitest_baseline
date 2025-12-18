"""
QUESTION:
Create a function that takes a string as input and returns the string in lowercase. If the input string is empty or contains non-alphabetic characters, return an empty string. Name the function `convert_to_lowercase`.
"""

def convert_to_lowercase(input_string):
    """
    This function converts a string to lowercase if it is not empty and contains only alphabetic characters.

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: The input string in lowercase if it is valid, otherwise an empty string.
    """
    if input_string.isalpha():
        return input_string.lower()
    else:
        return ""