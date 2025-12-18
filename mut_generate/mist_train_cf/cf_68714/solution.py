"""
QUESTION:
Write a function named `convert_to_snake_case` that transforms a given phrase into snake_case by replacing all spaces with underscores and converting all characters to lowercase. The input phrase is a string that may contain multiple words separated by spaces. The function should return the transformed string.
"""

def convert_to_snake_case(phrase):
    """
    Transforms a given phrase into snake_case by replacing all spaces with underscores and converting all characters to lowercase.

    Args:
        phrase (str): The input phrase to be transformed.

    Returns:
        str: The transformed string in snake_case.
    """
    return phrase.replace(" ", "_").lower()