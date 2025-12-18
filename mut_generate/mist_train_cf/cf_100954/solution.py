"""
QUESTION:
Develop a function named `replace_word` that takes a string `doc`, a target word `old_word`, and a replacement word `new_word` as input. The function should replace all occurrences of `old_word` in `doc` with `new_word`, ignoring variations in capitalization and ensuring that `old_word` is not part of a larger word. The function should return the modified string and a list of tuples, where each tuple contains the original position and length of each replaced instance of `old_word`.
"""

import re
def replace_word(doc, old_word, new_word):
    pattern = re.compile(r'\b' + re.escape(old_word) + r'\b', re.IGNORECASE)
    matches = [(m.start(), len(m.group())) for m in re.finditer(pattern, doc)]
    new_doc = re.sub(pattern, new_word, doc)
    return new_doc, matches