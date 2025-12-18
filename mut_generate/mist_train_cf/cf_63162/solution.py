"""
QUESTION:
Write a function called `lex_analyse` that takes a string as input. The string contains a sequence of characters with special characters, white spaces, and numeric strings. Disregard numeric strings and extract any instances of void textual elements or white spaces that exist both at the start and end of the given sequence, as well as between the lexical entities. The function should differentiate between whitespaces that are considered void textual elements and those that are a valid part of a word (e.g, in the case of hyphenated words). The function should return a list of separate lexical entities (words) as output.
"""

import re

def lex_analyse(str):
    pattern = r'\b[^\d\W]+\b|(?<=[^\s])-|-(?=[^\s])'
    return re.findall(pattern, str)