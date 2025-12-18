"""
QUESTION:
Create a function named `alphabetize_string` that takes a string as input and returns the string with its letters rearranged in alphabetical order. The function should work with any input string, regardless of its length or the case of its letters.
"""

def alphabetize_string(s):
    return ''.join(sorted(s))