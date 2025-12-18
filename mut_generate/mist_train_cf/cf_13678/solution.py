"""
QUESTION:
Write a function called `replace_chars` that takes in a string `text` and a dictionary `replace_dict`, where the dictionary contains the characters to replace and their corresponding replacements. The function should ignore any characters that are not part of the ASCII character set and only replace the specified characters in the string. The function should support Unicode strings.
"""

import unicodedata

def replace_chars(text, replace_dict):
    normalized_text = unicodedata.normalize('NFKD', text)  # Normalize Unicode string
    ascii_text = normalized_text.encode('ascii', 'ignore').decode()  # Remove non-ASCII characters

    for old_char, new_char in replace_dict.items():
        ascii_text = ascii_text.replace(old_char, new_char)  # Replace specified characters

    return ascii_text