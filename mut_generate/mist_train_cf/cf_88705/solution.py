"""
QUESTION:
Implement a function `search_engine(data, prefixes, suffixes, length)` that returns a list of words from `data` that are case-insensitively matched with all the prefixes in `prefixes`, contain at least one of the suffixes in `suffixes` (also case-insensitive), and have a length equal to `length`.
"""

def search_engine(data, prefixes, suffixes, length):
    results = []
    for word in data:
        if len(word) == length and all(prefix.lower() in word.lower() for prefix in prefixes) and any(suffix.lower() in word.lower() for suffix in suffixes):
            results.append(word)
    return results