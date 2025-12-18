"""
QUESTION:
Write a function `find_all_occurrences(text, word)` that takes two parameters: a text and a word. The function should return a list of indices where the word appears in the text, ignoring case-sensitivity and punctuation marks. The index position starts from 0.
"""

import re

def find_all_occurrences(text, word):
    """
    Returns a list of indices where the word appears in the text, 
    ignoring case-sensitivity and punctuation marks.

    Args:
    text (str): The input text.
    word (str): The word to search for.

    Returns:
    list: A list of indices where the word appears in the text.
    """
    cleaned_text = re.sub(r'[^\w\s]','',text.lower())  # Removing punctuation and converting to lower case
    words = cleaned_text.split()  # Splitting text into words on basis of space
    indices = [i for i, x in enumerate(words) if x == word.lower()]  # Finding indices of the word
    return indices