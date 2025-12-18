"""
QUESTION:
Create a function named `identify_language` that takes two parameters: `text` and `translations`. The function should identify the language of the given `text` based on the provided `translations` dictionary. The comparison between the `text` and `translations` should be case-insensitive and ignore any variations in punctuation or spacing. If the `text` matches a language in the `translations`, return the language; otherwise, return "Language not found."
"""

import re

def identify_language(text, translations):
    text = re.sub(r'[^\w\s]', '', text).lower()
    for language, translation in translations.items():
        if text == re.sub(r'[^\w\s]', '', translation).lower():
            return language
    return "Language not found."