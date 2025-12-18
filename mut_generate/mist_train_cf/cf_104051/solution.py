"""
QUESTION:
Write a function `remove_whitespace_punctuation_digits_and_convert_to_uppercase(text)` that takes a string `text` as input, removes all whitespace, punctuation, and digits from the string, and converts all remaining characters to uppercase.
"""

import string

def remove_whitespace_punctuation_digits_and_convert_to_uppercase(text):
    # Create a translation table that maps each character to None (to remove it)
    translation_table = str.maketrans('', '', string.whitespace + string.punctuation + string.digits)
    
    # Remove whitespace, punctuation, and digits, and convert to uppercase
    result = text.translate(translation_table).upper()
    
    return result