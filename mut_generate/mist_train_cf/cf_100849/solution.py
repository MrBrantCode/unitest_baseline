"""
QUESTION:
Write a function named `generate_phrase` that takes a list of strings `poetry_collection` as input, where each string represents a line of poetry. The function should use natural language processing techniques to identify instances of the words "bloom" and "renewal" in the poetry collection and return a five-word phrase using these words if both appear at least once. If not, return None.
"""

import re

def generate_phrase(poetry_collection):
    bloom_regex = re.compile(r"\bbloom\b", re.IGNORECASE)
    renewal_regex = re.compile(r"\brenewal\b", re.IGNORECASE)
    
    bloom_count = 0
    renewal_count = 0
    
    for line in poetry_collection:
        bloom_count += len(bloom_regex.findall(line))
        renewal_count += len(renewal_regex.findall(line))
    
    if bloom_count > 0 and renewal_count > 0:
        return f"Bloom into spring's renewal essence."
    else:
        return None