"""
QUESTION:
Create a function named `find_able_words` that takes a string as input and returns all words that end with "able" and are preceded by a digit, followed by a punctuation mark, and are not part of a larger word. The function should use regular expression to find the words.
"""

import re

def find_able_words(text):
    pattern = r"(?<!\w)\d\w*able\b(?!\w)"
    return re.findall(pattern, text)