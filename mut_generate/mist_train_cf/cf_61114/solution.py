"""
QUESTION:
Create a function named `replace_special_characters` that takes two parameters: a string `text` and a list of characters `special_characters`. The function should replace every instance of the characters in `special_characters` with a colon in the `text`. If `text` is `None` or empty, the function should return `text` as is. The function should also handle cases where the replacement character (colon) is part of `special_characters` and maintain the original case of alphabets in the text. The function should be efficient and able to handle large inputs and multiple languages with special characters.
"""

def replace_special_characters(text, special_characters):
    """
    Replaces every instance of special characters in the given text with a colon.

    Args:
    text (str): The input string to replace special characters from.
    special_characters (list): A list of special characters to be replaced.

    Returns:
    str: The text with special characters replaced.
    """
    # handling edge cases
    if text is None or len(text) == 0:
        return text
    # replacing each special character with colon
    for char in special_characters:
        text = text.replace(char, ':')
    return text