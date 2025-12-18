"""
QUESTION:
Implement a function named `search_engine` that takes four parameters: a list of words `data`, a list of prefixes `prefixes`, a list of suffixes `suffixes`, and a word length `length`. The function should return a list of words from `data` that are of the specified `length`, contain all the prefixes (case-insensitive), and contain at least one of the suffixes (case-insensitive).
"""

def search_engine(data, prefixes, suffixes, length):
    results = []
    for word in data:
        if len(word) == length and all(prefix.lower() in word.lower() for prefix in prefixes) and any(suffix.lower() in word.lower() for suffix in suffixes):
            results.append(word)
    return results