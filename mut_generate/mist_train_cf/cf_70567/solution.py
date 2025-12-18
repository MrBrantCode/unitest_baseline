"""
QUESTION:
Create a function named `remove_consecutive_duplicates` that takes a string `s` as input and returns a string with all consecutive repeating alphabetical characters removed.
"""

def remove_consecutive_duplicates(s):
    result = []
    for char in s:
        if result and char == result[-1]:
            continue
        result.append(char)
    return ''.join(result)