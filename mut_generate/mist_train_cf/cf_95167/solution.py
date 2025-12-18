"""
QUESTION:
Write a function `convert_string(string)` that takes a string as input, converts each non-vowel character to upper case and each vowel character to lower case, and returns the modified string.
"""

def convert_string(string):
    """
    This function converts each non-vowel character to upper case and each vowel character to lower case in a given string.

    Args:
        string (str): The input string.

    Returns:
        str: The modified string.
    """
    result = ""
    vowels = ["a", "e", "i", "o", "u"]
    for char in string:
        if char.lower() in vowels:
            result += char.lower()
        else:
            result += char.upper()
    return result