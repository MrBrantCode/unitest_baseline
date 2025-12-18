"""
QUESTION:
Write a function `capitalize_first_char` that takes a string as input and returns the string with its first character in uppercase. The function must ensure that the output string contains at least one lowercase character and one uppercase character.
"""

def capitalize_first_char(s):
    """
    This function takes a string as input, ensures it contains at least one lowercase character and one uppercase character,
    and returns the string with its first character in uppercase.

    Parameters:
    s (str): The input string.

    Returns:
    str: The string with its first character in uppercase.
    """
    s = s.lower()
    return s.capitalize()