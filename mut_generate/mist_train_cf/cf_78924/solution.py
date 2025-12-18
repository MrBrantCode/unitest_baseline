"""
QUESTION:
Write a function `find_hello_world(text)` that returns all occurrences of 'Hello World' in the provided text, ignoring any surrounding whitespace characters and considering the search case-insensitive. The function should return 'Hello World' (with the exact case) for each match found, regardless of the original case in the text.
"""

import re

def find_hello_world(text):
    pattern = re.compile(r'\s*(hello\s+world)\s*', re.I)
    matches = pattern.findall(text)

    return ['Hello World' if match.lower() == 'hello world' else match 
            for match in matches]