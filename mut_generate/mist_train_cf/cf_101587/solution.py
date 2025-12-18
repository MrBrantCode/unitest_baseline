"""
QUESTION:
Create a function `remove_word` that takes two parameters: `text` and `word`. The function should return the `text` after removing all occurrences of the `word`, regardless of case sensitivity or the presence of special characters surrounding the word.
"""

import re

def remove_word(text, word):
    pattern = re.compile(re.escape(word), re.IGNORECASE)
    return pattern.sub("", text)