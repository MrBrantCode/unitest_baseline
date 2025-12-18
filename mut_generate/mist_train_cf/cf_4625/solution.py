"""
QUESTION:
Write a function `split_string` that splits a given string into words. The function must handle multiple spaces, tabs, or newlines between words, ignore leading and trailing spaces, tabs, or newlines, and ignore punctuation marks. It should consider words with special characters, hyphens, underscores, apostrophes, parentheses, brackets, curly braces, quotation marks, digits, emojis, and special whitespace characters as a single word. The function should also handle words with mixed casing, different languages, and different character encodings, and it should efficiently split extremely long strings. The function must include comprehensive error handling and return an error message if the input string is empty or not a string.
"""

import re

def split_string(string):
    if not isinstance(string, str):
        return "Error: Input is not a string."

    string = string.strip()

    if not string:
        return "Error: Input string is empty."

    words = re.findall(r"\b[\w\-\_\'\(\)\[\]\{\}\d]+", string)

    return words