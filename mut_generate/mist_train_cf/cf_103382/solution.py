"""
QUESTION:
Implement a function `search_words_with_prefix(prefix, words)` that takes a prefix and a list of words as input and returns a list of words that contain the given prefix. Use recursion to solve this problem and assume the search is case-sensitive.
"""

def search_words_with_prefix(prefix, words):
    if not words:
        return []
    
    # Check if the first word in the list starts with the given prefix
    if words[0].startswith(prefix):
        return [words[0]] + search_words_with_prefix(prefix, words[1:])
    else:
        return search_words_with_prefix(prefix, words[1:])