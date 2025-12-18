"""
QUESTION:
Create a function called `remove_unnecessary_words` that uses regular expressions to remove words that start with a lowercase letter and are followed by a space from a given sentence.
"""

import re

def remove_unnecessary_words(sentence):
    pattern = r'\b[a-z]+\s'
    return re.sub(pattern, '', sentence)