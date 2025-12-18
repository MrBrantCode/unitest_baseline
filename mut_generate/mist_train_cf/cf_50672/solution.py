"""
QUESTION:
Write a function named `replace_whitespace` that takes a string as input and returns a string where all extra whitespace, newlines, and tabs are removed, single whitespace occurrences are replaced with underscores, and there are no consecutive underscores.
"""

import re

def replace_whitespace(text):
    text = ' '.join(text.split())
    text = text.replace(' ', '_')
    text = re.sub('_+', '_', text)
    return text