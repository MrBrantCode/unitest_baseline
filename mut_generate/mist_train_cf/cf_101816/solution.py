"""
QUESTION:
Write a function `replace_word(doc, old_word, new_word)` that replaces all occurrences of `old_word` in `doc` with `new_word` while keeping track of the original position and length of each instance. The function should ignore cases where `old_word` is part of a larger word and be case-insensitive. It should return the modified document and a list of tuples representing the original position and length of each replaced instance.
"""

import re

def replace_word(doc, old_word, new_word):
    pattern = re.compile(r'\b' + re.escape(old_word) + r'\b', re.IGNORECASE)
    matches = [(m.start(), len(m.group())) for m in re.finditer(pattern, doc)]
    new_doc = re.sub(pattern, new_word, doc)
    return new_doc, matches