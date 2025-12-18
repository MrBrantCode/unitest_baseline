"""
QUESTION:
Write a function named `capitalize_words` that takes a list of strings as input and returns a list of strings where the first letter of each word within each string is capitalized, while ignoring special characters. The function should handle strings that contain special characters.
"""

import re

def capitalize_words(strings):
    capitalized_strings = []
    for string in strings:
        cleaned_string = re.sub(r'[^A-Za-z\s]', '', string)
        capitalized_string = ' '.join(word.capitalize() for word in cleaned_string.split())
        capitalized_strings.append(capitalized_string)
    return capitalized_strings