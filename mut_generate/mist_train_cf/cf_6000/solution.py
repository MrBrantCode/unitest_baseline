"""
QUESTION:
Create a function called "hide_words" that takes an input text and a list of words to hide as parameters. The function should replace each word in the list with a specified symbol, such as asterisks (*), in a case-insensitive manner, preserving punctuation marks and special characters, and handling multiple occurrences and exact word matches.
"""

import re

def hide_words(text, words_to_hide):
    # Iterate through each word in the list of words to hide
    for word in words_to_hide:
        # Create a regular expression pattern to match the word as a whole word
        pattern = r'\b' + re.escape(word) + r'\b'
        # Replace all occurrences of the word with asterisks
        text = re.sub(pattern, '*' * len(word), text, flags=re.IGNORECASE)
    return text