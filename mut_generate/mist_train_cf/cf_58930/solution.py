"""
QUESTION:
Write a function `all_prefixes` that takes a string `str` as input and returns a list of all prefixes from shortest to longest. The prefixes should be ordered by their length, with the shortest prefix first.
"""

def all_prefixes(s):
    return [s[:i+1] for i in range(len(s))]