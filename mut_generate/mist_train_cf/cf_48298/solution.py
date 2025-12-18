"""
QUESTION:
Create a function `remove_vowels_digits_punctuation_whitespace_plus` that takes a string `text` as input and returns a modified string containing only English consonants, excluding vowels, digits, punctuation symbols, spaces, and non-English alphabets.
"""

def remove_vowels_digits_punctuation_whitespace_plus(text):
    """
    This function takes a string and returns a modified string free of vowels, digits, punctuation symbols, spaces, and non-English alphabets.

    Parameters:
    text (str): the input string

    Returns:
    output_text (str): the modified output string
    """
    output_text = ''
    for char in text:
        if char.lower() in 'bcdfghjklmnpqrstvwxyz':
            output_text += char
    return output_text