"""
QUESTION:
Create a function called `integrate_underscores` that takes a string `text` as input and returns the modified string with spaces replaced by underscores immediately after words that end with punctuation symbols. The function should be able to handle multiple punctuation marks and varying sentence structures.
"""

import re

def integrate_underscores(text):
    # find words followed by punctuation and replace the space after with '_'
    return re.sub(r'(\w+[\.,;:!?\)])( )', r'\1_', text)