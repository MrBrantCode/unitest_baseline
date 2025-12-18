"""
QUESTION:
Create a function called "hide_words" that takes two parameters: the input text and a list of words to hide. The function should replace all occurrences of the words to hide with asterisks, preserving punctuation and special characters, and handling cases where the words appear as part of other words. The function should be case-insensitive and handle multiple occurrences of the same word. The input text and words to hide will only contain letters and whitespace characters. The function should only replace exact word matches.
"""

import re

def hide_words(text, words_to_hide):
    for word in words_to_hide:
        pattern = r'\b' + re.escape(word) + r'\b'
        text = re.sub(pattern, '*' * len(word), text, flags=re.IGNORECASE)
    return text