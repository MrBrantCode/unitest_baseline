"""
QUESTION:
Create a function named `find_ing_words` that takes a string `text` as input and returns a list of all words in the text that end with the suffix "ing". The function should be able to match words of any length and regardless of their preceding characters.
"""

import re 

def find_ing_words(text):
    pattern = r'\b(\w+ing)\b'
    return re.findall(pattern, text)