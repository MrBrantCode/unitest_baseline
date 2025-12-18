"""
QUESTION:
Write a function `generate_phrase` that generates a five-word phrase based on the presence of the words "bloom" and "renewal" in a given poetry collection. The phrase should be "Bloom into spring's renewal essence" if both words appear at least once in the collection. The function should take a list of strings as input, where each string represents a line of poetry. If either "bloom" or "renewal" does not appear in the collection, the function should return None.
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