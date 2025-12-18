"""
QUESTION:
Create a function named `replace_word` that takes a string, a word to replace, and a replacement word as input. The function must replace all occurrences of the word to replace in the string with the replacement word in a case-insensitive manner. The function should handle strings that contain punctuation marks and special characters, as well as replacement words that contain punctuation marks or special characters.
"""

import re

def replace_word(string, word_to_replace, replacement_word):
    # Create a regular expression pattern to match the word to replace
    pattern = re.compile(r'\b' + re.escape(word_to_replace) + r'\b', re.IGNORECASE)

    # Replace the word using the regular expression pattern
    result = re.sub(pattern, replacement_word, string)

    return result