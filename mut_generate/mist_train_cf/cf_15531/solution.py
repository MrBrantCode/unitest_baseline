"""
QUESTION:
Create a function `find_word(word, text)` that determines if a specific word is present in a given text. The function should return "Word found" if the word is found, and "Word not found" otherwise. The solution should be optimized for performance.
"""

def find_word(word, text):
    if word in text:
        return "Word found"
    else:
        return "Word not found"