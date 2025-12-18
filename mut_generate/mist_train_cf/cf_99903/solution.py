"""
QUESTION:
Create a function named `replace_word` that takes a text document (`doc`), an old word (`old_word`), and a new word (`new_word`) as input. The function should replace all instances of `old_word` in `doc` with `new_word` (ignoring case and ensuring `old_word` is a whole word) and return a tuple containing the modified document and a list of tuples representing the original position and length of each replaced instance.
"""

import re

def replace_word(doc, old_word, new_word):
    pattern = re.compile(r'\b' + re.escape(old_word) + r'\b', re.IGNORECASE)
    matches = [(m.start(), len(m.group())) for m in re.finditer(pattern, doc)]
    new_doc = re.sub(pattern, new_word, doc)
    return new_doc, matches