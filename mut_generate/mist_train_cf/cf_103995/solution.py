"""
QUESTION:
Write a function named `letter_frequency` that takes a string `text` as input and returns a dictionary with letters as keys and their frequencies as values. The function should ignore case sensitivity, non-alphabetic characters, and count the frequency of each letter. The output dictionary should be sorted in descending order of letter frequencies.
"""

from collections import Counter
import re

def letter_frequency(text):
    """
    Returns a dictionary with letters as keys and their frequencies as values.
    
    The function ignores case sensitivity, non-alphabetic characters, and counts the frequency of each letter.
    The output dictionary is sorted in descending order of letter frequencies.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary with letters as keys and their frequencies as values.
    """
    cleaned_text = re.sub(r'[^a-zA-Z]', '', text.lower())
    letter_count = Counter(cleaned_text)
    return dict(sorted(letter_count.items(), key=lambda x: x[1], reverse=True))