"""
QUESTION:
Create a function called `replace_vowels` that takes a string and a replacement character as input. The function should replace all the vowels in the string with the given replacement character. The vowels are 'a', 'e', 'i', 'o', and 'u', and the replacement should be case-insensitive. Return the modified string.
"""

def replace_vowels(string, replacement_character):
    """
    Replaces all the vowels in the given string with the given replacement character.

    Args:
        string (str): The input string.
        replacement_character (str): The character to replace the vowels with.

    Returns:
        str: The modified string with all vowels replaced.
    """
    vowels = 'aeiouAEIOU'
    return ''.join(replacement_character if char in vowels else char for char in string)