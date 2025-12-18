"""
QUESTION:
Design a function named `filter_special_chars` that takes a string input `text` and returns a new string with all special characters, including emojis, removed. The function should preserve the order of the remaining characters and not consider whitespace as a special character. The function should be able to handle common emojis, but does not need to handle all possible emojis.
"""

import re

def filter_special_chars(text):
    pattern = re.compile(r"[^\w\s]|[\u263a-\U0001f645]")
    filtered_text = re.sub(pattern, "", text)
    return filtered_text