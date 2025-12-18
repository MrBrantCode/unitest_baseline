"""
QUESTION:
Create a function `replace_word(doc, old_word, new_word)` that replaces all occurrences of `old_word` in `doc` with `new_word` regardless of capitalization, and returns the modified document along with a list of tuples representing the original position and length of each replaced instance. The function should only match whole words, excluding occurrences that are part of larger words.
"""

import re
def replace_word(doc, old_word, new_word):
    pattern = re.compile(r'\b' + re.escape(old_word) + r'\b', re.IGNORECASE)
    matches = [(m.start(), len(m.group())) for m in re.finditer(pattern, doc)]
    new_doc = re.sub(pattern, new_word, doc)
    return new_doc, matches