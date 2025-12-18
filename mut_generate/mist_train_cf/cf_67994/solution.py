"""
QUESTION:
Create a function named `extract_identity` that takes a string `text` as input. This function should return a string representing a complete personal identity, including given name, middle name (if present), and surname, from the input `text`. The function should accommodate individuals with multiple middle names or hyphenated surnames, and it should return `None` if no match is found.
"""

import re

def extract_identity(text):
    pattern = r"([A-Za-z]+(?: [A-Za-z-]+){1,3})"
    matches = re.findall(pattern, text)
    return matches[0] if matches else None