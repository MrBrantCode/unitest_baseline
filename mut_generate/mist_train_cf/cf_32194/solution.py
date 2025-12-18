"""
QUESTION:
Write a function `count_word_occurrences` that takes two parameters: `input_string` and `target_word`. The function should return the count of all occurrences of the target word within the input string, ignoring case and considering only whole word matches. The function should also ignore any punctuation or special characters present in the input string.
"""

import re

def count_word_occurrences(input_string, target_word):
    clean_string = re.sub(r'[^\w\s]', '', input_string).lower()
    occurrences = re.findall(r'\b' + re.escape(target_word.lower()) + r'\b', clean_string)
    return len(occurrences)