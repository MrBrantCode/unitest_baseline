"""
QUESTION:
Create a function `remove_sequence` that takes a string `s` as input and returns the string with all instances of "abcd" removed. The function should be able to handle cases where "abcd" appears multiple times in the string, with or without spaces in between.
"""

def remove_sequence(s):
    return s.replace('abcd', '')