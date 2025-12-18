"""
QUESTION:
Create a function `find_overlapping_indices(string, substring)` that returns all the indices in a string where a given substring occurs, allowing for overlapping matches. The function should handle substrings with special characters or symbols and be case-insensitive.
"""

def find_overlapping_indices(string, substring):
    indices = []
    start = 0
    while True:
        index = string.lower().find(substring.lower(), start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1
    return indices