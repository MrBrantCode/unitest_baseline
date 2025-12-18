"""
QUESTION:
Create a function called `capitalize_first_char` that takes a string as input and returns the string with the first character changed to uppercase. The function should not modify the original string. The input string is guaranteed to be non-empty.
"""

def capitalize_first_char(s):
    """
    This function takes a string as input, capitalizes the first character, 
    and returns the modified string without changing the original string.

    Parameters:
    s (str): The input string.

    Returns:
    str: The input string with the first character capitalized.
    """
    return s[0].upper() + s[1:]