"""
QUESTION:
Write a function `compare_strings` that takes two strings as input and returns the longer string. The function should be able to handle strings of up to 1 million characters.
"""

def compare_strings(string1, string2):
    if len(string1) > len(string2):
        return string1
    else:
        return string2