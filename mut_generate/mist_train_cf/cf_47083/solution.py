"""
QUESTION:
Develop a function named `analyze_text` that accepts a text input and returns a dictionary containing categories of non-alphanumeric characters, including 'whitespace', 'punctuation', and 'special symbol', along with their frequencies.
"""

import re
from collections import Counter

def analyze_text(text):
    non_alphanum = re.findall(r'\W', text)
    counts = Counter(non_alphanum)

    categories = {
        'whitespace': [],
        'punctuation': [],
        'special symbol': [],
    }
    for char, count in counts.items():
        if char.isspace():
            categories['whitespace'].append((char, count))
        elif char.isprintable():
            categories['punctuation'].append((char, count))
        else:
            categories['special symbol'].append((char, count))

    return categories