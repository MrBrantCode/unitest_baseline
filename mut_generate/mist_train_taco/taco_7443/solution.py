"""
QUESTION:
Given a string of words (x), you need to return an array of the words, sorted alphabetically by the final character in each.

If two words have the same last letter, they returned array should show them in the order they appeared in the given string.

All inputs will be valid.
"""

def sort_words_by_last_char(x: str) -> list:
    return sorted(x.split(), key=lambda word: word[-1])