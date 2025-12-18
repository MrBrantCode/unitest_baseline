"""
QUESTION:
Create a function named `distinct_lexemes` that takes a text string as input, removes punctuation, and converts the text to lowercase. The function should then split the text into words and return a set of distinct words, ignoring duplicates and case differences.
"""

import string

def distinct_lexemes(text):
    # Remove punctuation from the text
    for p in string.punctuation:
        text = text.replace(p, '')
        
    # Lowercase the text to manage case differentiations
    text = text.lower()

    # Split the text into words and accumulate them in a set to get the distinct lexemes
    lexemes = set(text.split())

    return lexemes