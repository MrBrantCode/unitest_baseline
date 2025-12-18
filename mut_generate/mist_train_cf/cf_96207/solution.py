"""
QUESTION:
Write a function `sort_strings` that takes a list of strings as input and returns a new list with duplicates removed and the remaining strings sorted in descending order of length. If two or more strings have the same length, they should be sorted in alphabetical order. The function should be able to handle lists of up to 1 million strings, with each string having a length of up to 100 characters.
"""

def sort_strings(strings):
    return sorted(set(strings), key=lambda x: (-len(x), x))