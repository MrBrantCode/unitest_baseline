"""
QUESTION:
Create a function named `replace_abbreviations` that takes a string `text` and a dictionary `abbreviations` as input. The function should replace all occurrences of the abbreviations in the dictionary with their corresponding full forms in the text, while preserving the original tense and grammatical structure. The function should return the modified text.
"""

import re

def replace_abbreviations(text, abbreviations):
    # Use regular expressions to find all abbreviations in the text
    regex = re.compile(r'\b(' + '|'.join(abbreviations.keys()) + r')\b')
    matches = regex.findall(text)

    # Replace all abbreviations with their full forms
    for match in matches:
        full_form = abbreviations[match]
        text = re.sub(r'\b' + match + r'\b', full_form, text)

    return text