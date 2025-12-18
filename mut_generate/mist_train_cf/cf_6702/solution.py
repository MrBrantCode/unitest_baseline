"""
QUESTION:
Create a regular expression pattern for a function named `find_able_words` that finds all words ending with "able" in a string. The word "able" should be preceded by a digit followed by a punctuation mark (.,!?), and it should not be part of a larger word. Additionally, ensure that the word "able" is not immediately followed by another word starting with the same letter.
"""

import re

def find_able_words(s):
    pattern = r'(?<=\d[.,!?])\b\w*(?<!\b\w)able\b(?!s?\b\w)'
    return re.findall(pattern, s)