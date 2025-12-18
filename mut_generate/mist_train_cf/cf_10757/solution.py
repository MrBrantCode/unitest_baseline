"""
QUESTION:
Write a function `find_last_occurrence` that takes a string `s` and a substring `target` as input, and returns the index of the last occurrence of `target` in `s`. If `target` does not exist in `s`, return -1.
"""

def find_last_occurrence(s, target):
    try:
        return s.rindex(target)
    except ValueError:
        return -1