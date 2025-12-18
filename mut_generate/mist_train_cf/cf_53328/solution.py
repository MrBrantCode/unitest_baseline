"""
QUESTION:
Create a function named `find_ing_ending_words` that takes a string as input and returns a list of all words that end with the letter sequence "ing". The function should correctly distinguish between words that end with "ing" and words that contain "ing" in the middle. The function should use regular expressions to achieve this.
"""

import re

def find_ing_ending_words(text):
    pattern = r'\b\w*ing\b'
    matches = re.findall(pattern, text)
    return matches