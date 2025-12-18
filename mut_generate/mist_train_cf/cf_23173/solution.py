"""
QUESTION:
Write a regular expression to match the word "she" as a standalone word in a sentence, allowing for case-insensitive matching. The regular expression should ensure that "she" is not matched as part of another word.
"""

import re

def find_she(sentence):
    """
    Counts the number of times the word 'she' appears in a sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        int: The number of times 'she' appears in the sentence.
    """
    pattern = r'\b[sS]he\b'
    return len(re.findall(pattern, sentence))