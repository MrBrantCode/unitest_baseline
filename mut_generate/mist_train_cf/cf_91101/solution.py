"""
QUESTION:
Write a function named `match_the_quick` to match a substring 'the' within a sentence but only if it is followed by the word 'quick' and preceded by a word that starts with a capital letter, using regular expressions in Python. The function should return all matches from the given sentence.

The function should be able to handle any string input as a sentence.
"""

import re

def match_the_quick(sentence):
    """
    This function matches a substring 'the' within a sentence, 
    only if it is followed by the word 'quick' and preceded by a word that starts with a capital letter.

    Args:
        sentence (str): The input sentence to search for matches.

    Returns:
        list: A list of matches found in the sentence.
    """
    pattern = r'\b[A-Z][a-zA-Z]* the quick\b'
    matches = re.findall(pattern, sentence)
    return matches