"""
QUESTION:
Create a function named `remove_duplicates` that takes a string as input and returns the modified string with all consecutive duplicate characters removed. If a character appears multiple times in a row, only the first occurrence should be kept. If the string is empty or contains no duplicated characters, return the original string.
"""

def remove_duplicates(s):
    result = []
    for char in s:
        if not result or char != result[-1]:
            result.append(char)
    return ''.join(result)