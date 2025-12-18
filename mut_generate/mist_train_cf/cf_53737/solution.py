"""
QUESTION:
Create a function `find_words_starting_with_A` that takes a string `text` as input and returns a list of words that start with the uppercase letter "A". The function should use regular expressions to identify the words.
"""

import re 

def find_words_starting_with_A(text):
    pattern = r"\bA\w*\b"
    words_starting_with_A = re.findall(pattern, text)
    return words_starting_with_A