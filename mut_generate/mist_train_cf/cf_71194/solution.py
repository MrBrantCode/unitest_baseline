"""
QUESTION:
Implement a function `unique_substrings(string, size)` that extracts unique substrings of a specified size from a given string, maintaining their original order. The function should return an error message if the specified size is greater than the string length.
"""

def unique_substrings(string, size):
    if size > len(string):
        return "Error: substring size is greater than string length."
    strings = []
    for i in range(len(string)-size+1):
        substring = string[i : i+size]
        if substring not in strings:
            strings.append(substring)
    return strings