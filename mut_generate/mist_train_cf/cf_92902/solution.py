"""
QUESTION:
Write a function `replace_chars` that takes two parameters: `text` and `replace_dict`. `text` is a string that may contain Unicode characters and `replace_dict` is a dictionary where keys are the characters to be replaced and values are their corresponding replacements. The function should return the modified string with all non-ASCII characters removed and the specified characters replaced according to `replace_dict`. The function should be compatible with Python 3.x.
"""

import unicodedata

def replace_chars(text, replace_dict):
    normalized_text = unicodedata.normalize('NFKD', text)  # Normalize Unicode string
    ascii_text = normalized_text.encode('ascii', 'ignore').decode()  # Remove non-ASCII characters

    for old_char, new_char in replace_dict.items():
        ascii_text = ascii_text.replace(old_char, new_char)  # Replace specified characters

    return ascii_text