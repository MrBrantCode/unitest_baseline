"""
QUESTION:
Write a function `replace_abbreviations` that takes a string `text` and a dictionary `abbreviations` as input, where the keys are abbreviations and the values are their full forms. Replace all occurrences of the abbreviations in the text with their full forms, maintaining the same tense and grammatical structure. The function should return the modified text.
"""

import re

def replace_abbreviations(text, abbreviations):
    """
    Replace abbreviations in a given text with their full forms while maintaining the same tense and grammatical structure.

    Args:
        text (str): The input text containing abbreviations.
        abbreviations (dict): A dictionary of abbreviations and their full forms.

    Returns:
        str: The modified text with abbreviations replaced.
    """

    # Use regular expressions to find all abbreviations in the text
    regex = re.compile(r'\b(' + '|'.join(abbreviations.keys()) + r')\b')
    matches = regex.findall(text)

    # Replace all abbreviations with their full forms
    for match in matches:
        full_form = abbreviations[match]
        text = re.sub(r'\b' + match + r'\b', full_form, text)

    return text