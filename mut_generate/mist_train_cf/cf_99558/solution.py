"""
QUESTION:
Write a function named `replace_word` that takes three parameters: `doc`, `old_word`, and `new_word`. The function should replace all occurrences of `old_word` in `doc` with `new_word` and return the modified document along with a list of tuples representing the original position and length of each replaced instance. The function should ignore any occurrences of `old_word` that are part of larger words and should be case-insensitive.
"""

import re
def replace_word(doc, old_word, new_word):
    pattern = re.compile(r'\b' + re.escape(old_word) + r'\b', re.IGNORECASE)
    matches = [(m.start(), len(m.group())) for m in re.finditer(pattern, doc)]
    new_doc = re.sub(pattern, new_word, doc)
    return new_doc, matches