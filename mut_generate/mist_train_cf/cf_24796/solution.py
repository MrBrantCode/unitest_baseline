"""
QUESTION:
Write a function to capitalize the first letter of each word in a given string. The function should take a string as input and return the modified string.
"""

def capitalize_first_letters(input_string):
    """
    Capitalize the first letter of each word in a given string.

    Args:
        input_string (str): The input string.

    Returns:
        str: The modified string with capitalized first letter of each word.
    """
    return ' '.join(word.capitalize() for word in input_string.split())