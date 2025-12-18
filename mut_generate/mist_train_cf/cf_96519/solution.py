"""
QUESTION:
Find the index of the first occurrence of a given word in a text, ignoring case and ensuring the word is not part of a larger word. The function should handle cases where the word is followed by punctuation marks. The input is a text string and a word string, and the output is the index of the first occurrence of the word if found, or -1 if not found.
"""

import re

def entrance(text, word):
    text = text.lower()
    word = word.lower()
    match = re.search(r'\b' + re.escape(word) + r'\b', text)
    if match:
        return match.start()
    else:
        return -1