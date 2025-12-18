"""
QUESTION:
Create a function `snake_case(s)` that transforms an English sentence into snake_case format. The function should handle multiple sentences (multi-line strings), remove punctuation and special characters, lowercase all characters, and separate words with underscores.
"""

import re

def snake_case(s):
    # Remove punctuation and special characters
    s = re.sub(r'[^a-zA-Z0-9\s]', '', s)
    # Transform multiple spaces into one
    s = re.sub(r'\s+', ' ', s)
    # Transform space into underscore and lowercase all characters
    s = s.replace(' ', '_').lower()

    return s