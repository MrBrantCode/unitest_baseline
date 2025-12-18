"""
QUESTION:
Create a function named `find_occurrences` that takes a string `text` as input and returns a list of tuples, each containing a string and its starting index in the input text. The string should match the phrase "hello people" regardless of case, with the following restrictions: 
- the function should use regular expressions to identify the matches
- the matches should be whole words, not parts of other words.
"""

import re

def find_occurrences(text):
    pattern = re.compile(r'\b[Hh][Ee][Ll]{2}[Oo] [Pp][Ee][Oo][Pp][Ll][Ee]\b')
    matches = pattern.finditer(text)
    return [(match.group(), match.start()) for match in matches]