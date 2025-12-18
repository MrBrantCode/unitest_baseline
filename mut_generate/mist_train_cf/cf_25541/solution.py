"""
QUESTION:
Write a function `replace_vowels` that takes a string as input and returns a new string where all vowels ('a', 'e', 'i', 'o', 'u') are replaced with a star (*).
"""

def replace_vowels(string):
    """
    This function replaces all vowels in a given string with a star (*).

    Args:
        string (str): The input string.

    Returns:
        str: A new string where all vowels are replaced with a star (*).
    """
    return ''.join([x if x.lower() not in 'aeiou' else '*' for x in string])