"""
QUESTION:
Write a function `match_the_quick` that uses regex to find a substring 'the' in a sentence. The function should match 'the' only if it is preceded by a word starting with a capital letter and immediately followed by the word 'quick'. The sentence should not contain any other occurrences of 'the'.
"""

import re

def match_the_quick(sentence):
    """
    This function uses regex to find a substring 'the' in a sentence.
    The function matches 'the' only if it is preceded by a word starting with a capital letter 
    and immediately followed by the word 'quick'. The sentence should not contain any other occurrences of 'the'.

    Args:
        sentence (str): The input sentence.

    Returns:
        bool: True if the sentence meets the specified conditions, False otherwise.
    """

    # Check if 'the' is not present elsewhere in the sentence
    if sentence.lower().count('the') > 1:
        return False

    # Use regex to find 'the' preceded by a word starting with a capital letter and followed by 'quick'
    pattern = r'\b[A-Z]\w*\bthe\b(?=\squick\b)'
    match = re.search(pattern, sentence)

    # Return True if a match is found, False otherwise
    return match is not None