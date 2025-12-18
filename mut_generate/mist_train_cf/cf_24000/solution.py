"""
QUESTION:
Write a function `camel_case_string` that converts a given string in camelCase notation to snake_case notation. The input string will only contain alphanumeric characters and uppercase letters will denote the start of a new word in camelCase notation. The function should return a string in snake_case notation.
"""

def camel_case_string(s: str) -> str:
    """
    Converts a given string in camelCase notation to snake_case notation.

    Args:
        s (str): The input string in camelCase notation.

    Returns:
        str: The input string converted to snake_case notation.
    """

    # Initialize an empty string to store the result
    result = ""

    # Iterate over each character in the input string
    for i, char in enumerate(s):
        # If the character is uppercase and it's not the first character in the string
        if char.isupper() and i != 0:
            # Append an underscore before the character
            result += "_" + char.lower()
        else:
            # Otherwise, just append the lowercase character
            result += char.lower()

    # Return the result
    return result