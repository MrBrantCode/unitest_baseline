"""
QUESTION:
Write a function `replace_python_with_programming` that takes a string as an argument and returns the string with all occurrences of the word "Python" (case-insensitive) replaced with "Programming" and all punctuation marks removed. If the string does not contain the word "Python", return the original string with punctuation marks removed. The function should also remove any leading or trailing whitespaces from the string.
"""

import re

def replace_python_with_programming(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = text.strip()
    if re.search(r'\bpython\b', text, re.IGNORECASE):
        text = re.sub(r'\bpython\b', 'Programming', text, flags=re.IGNORECASE)
    return text