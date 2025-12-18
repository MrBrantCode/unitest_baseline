"""
QUESTION:
Develop a function `is_consonant_only(word)` that determines if a given word consists solely of consonants, handling cases of double consonants, capitalization, and words with special characters and numbers. The function should return `True` if the word only contains consonants, and `False` otherwise.
"""

import re

def is_consonant_only(word):
    pattern = '^[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]+$'
    if re.match(pattern, word):
        return True
    else:
        return False