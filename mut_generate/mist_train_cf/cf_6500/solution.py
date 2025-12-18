"""
QUESTION:
Implement the `replace_placeholders` function, which takes a string and a dictionary of placeholder words as input, and returns the string with all occurrences of the placeholder words replaced while maintaining their original capitalization. The replacement should be case-sensitive, handling different capitalization forms of the same placeholder word.
"""

def replace_placeholders(text, dictionary):
    """
    Replace placeholder words in a given text with their corresponding values while maintaining their original capitalization.

    Args:
        text (str): The input text containing placeholder words.
        dictionary (dict): A dictionary containing placeholder words as keys and their replacement values as values.

    Returns:
        str: The text with all occurrences of placeholder words replaced.
    """
    for placeholder, value in dictionary.items():
        text = text.replace(placeholder, value)
        text = text.replace(placeholder.capitalize(), value.capitalize())
        text = text.replace(placeholder.upper(), value.upper())
        text = text.replace(placeholder.lower(), value.lower())
    return text