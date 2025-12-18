"""
QUESTION:
Create a function called `find_overlapping_indices` that takes two parameters: a string and a substring. The function should return a list of indices where the substring occurs in the string, considering overlapping occurrences and handling special characters, symbols, and cases with a combination of uppercase and lowercase letters.
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