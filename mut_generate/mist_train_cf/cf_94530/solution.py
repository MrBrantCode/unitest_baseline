"""
QUESTION:
Create a function called `capitalize_words` that takes a list of strings as input. The function should return a list of strings where the first letter of each word in each string is capitalized, and all special characters are removed. Special characters include any character that is not a letter or a whitespace character.
"""

import re

def capitalize_words(strings):
    capitalized_strings = []
    for string in strings:
        cleaned_string = re.sub(r'[^A-Za-z\s]', '', string)
        capitalized_string = ' '.join(word.capitalize() for word in cleaned_string.split())
        capitalized_strings.append(capitalized_string)
    return capitalized_strings