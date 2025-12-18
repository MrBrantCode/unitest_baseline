"""
QUESTION:
Write a regular expression to match the entire sentence "Mary had a little lamb that followed her everywhere she went and it was very cute." exactly, ensuring it is not part of a larger sentence.
"""

import re

def match_sentence(text):
    pattern = r'\b(Mary had a little lamb that followed her everywhere she went and it was very cute)\b'
    match = re.match(pattern, text)
    return bool(match)

# Note: You can call this function with your sentence as an argument.