"""
QUESTION:
Write a function named `extract_strings` that takes a text block as input and returns a list of strings that match the regex pattern "name #number", where the name can be any alphanumeric characters and the number is a 4-digit integer. The extracted strings should be sorted in descending order based on the number. The function should return an empty list if no match is found.
"""

import re

def extract_strings(text):
    pattern = r"([a-zA-Z0-9]+)\s#(\d{4})"
    matches = re.findall(pattern, text)
    sorted_matches = sorted(matches, key=lambda x: int(x[1]), reverse=True)
    return sorted_matches