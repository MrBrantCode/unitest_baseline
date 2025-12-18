"""
QUESTION:
Write a function named `generate_phrase` that takes a list of strings representing lines of poetry as input. The function should use the words "bloom" and "renewal" to generate a phrase if both words appear at least once in the poetry collection. If both words are found, return the phrase "Bloom into spring's renewal essence." Otherwise, return None.
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
        return "Bloom into spring's renewal essence."
    else:
        return None