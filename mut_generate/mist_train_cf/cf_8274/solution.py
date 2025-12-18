"""
QUESTION:
Write a function named `find_substring` that takes two parameters, `text` and `pattern`, and returns a list of all starting indices where `pattern` is found within `text`. The function should return an empty list if `pattern` is not found in `text`. The function should handle cases where `pattern` appears multiple times within `text`.
"""

def find_substring(text, pattern):
    indices = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            indices.append(i)
    return indices