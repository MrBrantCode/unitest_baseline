"""
QUESTION:
Split a given string into words. The function should be named `split_string` and it should handle multiple spaces, tabs, or newlines between words, ignore leading and trailing spaces, tabs, or newlines in the input string, and handle various special cases including punctuation marks, hyphens, underscores, apostrophes, parentheses, brackets, curly braces, quotation marks, special characters, non-alphanumeric characters, digits, emojis, and special whitespace characters. The function should also handle mixed casing, different languages, and extremely long strings efficiently. If the input string is empty or not a string, the function should return an error message.
"""

import re

def split_string(input_string):
    # Check if input_string is empty or not a string
    if not isinstance(input_string, str) or len(input_string) == 0:
        return "Input string is empty or not a string."
    
    # Remove leading and trailing spaces, tabs, and newlines
    input_string = input_string.strip()
    
    # Split the string into words using regular expressions
    words = re.findall(r'\b\w[\w\-\']*\b', input_string)
    
    return words