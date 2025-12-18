"""
QUESTION:
Create a function `find_words` that takes a string of text as input. The function should return a list of words that contain the letters 'x' and 'y' consecutively, with 'x' and 'y' appearing only once in the word, and the word length not exceeding six characters.
"""

import re

def find_words(text):
    pattern = r'\b[a-zA-Z]*xy[a-zA-Z]*\b'
    matching_words = [word for word in text.split() if re.fullmatch(pattern, word) and len(word) <= 6 and word.count('x') == 1 and word.count('y') == 1]
    return matching_words