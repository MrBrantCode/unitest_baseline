"""
QUESTION:
Create a function `assert_unique_chars` that takes a string `text_sequence` as input. The function should check if all alphabetical characters in the string are unique, ignoring case, non-alphabetical characters, and spaces. It should return `True` if all alphabetical characters are unique and `False` otherwise.
"""

def assert_unique_chars(text_sequence):
    # remove white spaces (if considering them as non-alphabetical components)
    text_sequence = text_sequence.replace(" ", "")

    # to make it case-insensitive
    text_sequence = text_sequence.lower()
    
    # consider only alphabetical characters
    text_sequence = ''.join(c for c in text_sequence if c.isalpha())

    is_unique = len(set(text_sequence)) == len(text_sequence)
    return is_unique