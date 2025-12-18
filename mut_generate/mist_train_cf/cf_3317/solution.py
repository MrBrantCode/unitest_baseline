"""
QUESTION:
Create a function called `remove_whitespace_and_punctuation` that takes a string as input and returns a string with all whitespace characters and punctuation marks removed, while ignoring case sensitivity and preserving non-English characters and special characters like emojis. The function should handle multibyte characters properly. The input string can contain any characters, including whitespace, punctuation, alphanumeric characters, special characters, and non-English characters. The output string should only contain alphanumeric characters, special characters, and non-English characters, all in lowercase.
"""

import unicodedata

def remove_whitespace_and_punctuation(string):
    whitespace_chars = [' ', '\t', '\n', '\r']
    punctuation_chars = [chr(i) for i in range(33, 127) if not chr(i).isalnum()]

    string = unicodedata.normalize('NFD', string)
    string = ''.join(char for char in string if char not in whitespace_chars and char not in punctuation_chars)
    string = string.lower()
    string = unicodedata.normalize('NFC', string)

    return string