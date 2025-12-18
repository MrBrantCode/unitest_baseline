"""
QUESTION:
Create a function called `find_email` to extract email addresses from a given text. The function should identify email addresses that end with .edu or .gov domains. The function should return a list of matched email addresses.
"""

import re

def find_email(text):
    pattern = r"\b[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9-]+\.)+(edu|gov)\b"
    return re.findall(pattern, text)