"""
QUESTION:
Create a function named `tokenize_string` that takes a string as input and returns a list of strings, where each string represents a word in the original string. The function should ignore leading and trailing whitespace in each word, handle contractions, possessive forms, hyphenated words, and words with special characters correctly. It should also handle multiple consecutive whitespace characters as a single delimiter, empty strings, strings containing multiple languages and character sets, and complex sentence structures. The function should be case-insensitive and efficient for very long strings.
"""

import re

def tokenize_string(string):
    # Remove leading and trailing whitespace
    string = string.strip()
    
    # If the string is empty, return an empty list
    if not string:
        return []
    
    # Use regular expression to split the string into words
    words = re.findall(r'\w+[\w\'@-]*\w+|\w', string.lower())
    
    return words