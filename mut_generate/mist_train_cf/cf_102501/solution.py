"""
QUESTION:
Write a function named `find_index` that takes a list of strings `strings` and a target string `target` as parameters. The function should return the index of the first occurrence of `target` in `strings` if found, and -1 if not found. The function should be case-sensitive, treat empty strings as valid inputs, and handle lists with at least 100 strings, where each string is 50 characters or less in length.
"""

def find_index(strings, target):
    for i, string in enumerate(strings):
        if string == target:
            return i
    return -1