"""
QUESTION:
Write a function called `compare_strings` that takes two strings as input and returns the longer one. The input strings can contain up to 1 million characters.
"""

def compare_strings(string1, string2):
    if len(string1) > len(string2):
        return string1
    else:
        return string2