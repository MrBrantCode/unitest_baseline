"""
QUESTION:
Create a function called `check_and_replace_string` that takes a string as input, removes all punctuation marks, and checks if the string contains the word "Python" in a case-insensitive manner. If the word "Python" is found, replace all occurrences of it with "Programming". If not found, return the original string without punctuation marks.
"""

import re

def check_and_replace_string(s):
    s = re.sub(r'[^\w\s]', '', s)
    if re.search(r'\bpython\b', s, re.IGNORECASE):
        s = re.sub(r'\bpython\b', 'Programming', s, flags=re.IGNORECASE)
    return s